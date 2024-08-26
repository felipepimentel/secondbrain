import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from secondbrain.document_processor import process_document
from secondbrain.weaviate_client import WeaviateClient

class FolderHandler(FileSystemEventHandler):
    def __init__(self, weaviate_client):
        self.weaviate_client = weaviate_client

    def on_created(self, event):
        if not event.is_directory:
            self.process_file(event.src_path)

    def on_modified(self, event):
        if not event.is_directory:
            self.process_file(event.src_path)

    def on_deleted(self, event):
        if not event.is_directory:
            self.weaviate_client.delete_document(event.src_path)

    def process_file(self, file_path):
        processed_data = process_document(file_path)
        self.weaviate_client.index_document(processed_data)

class FolderSync:
    def __init__(self, folder_path, weaviate_client):
        self.folder_path = folder_path
        self.weaviate_client = weaviate_client
        self.observer = Observer()

    def start(self):
        event_handler = FolderHandler(self.weaviate_client)
        self.observer.schedule(event_handler, self.folder_path, recursive=True)
        self.observer.start()

    def stop(self):
        self.observer.stop()
        self.observer.join()

    def run(self):
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()