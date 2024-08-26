import click
from secondbrain.folder_sync import FolderSync
from secondbrain.weaviate_client import WeaviateClient
from secondbrain.search_engine import SearchEngine

@click.group()
def cli():
    pass

@cli.command()
@click.argument('folder_path')
def sync(folder_path):
    weaviate_client = WeaviateClient("http://localhost:8080")
    folder_sync = FolderSync(folder_path, weaviate_client)
    click.echo(f"Starting synchronization for folder: {folder_path}")
    folder_sync.run()

@cli.command()
@click.argument('query')
def search(query):
    weaviate_client = WeaviateClient("http://localhost:8080")
    search_engine = SearchEngine(weaviate_client)
    results = search_engine.search(query)
    for result in results:
        click.echo(f"Path: {result['path']}")
        click.echo(f"Content: {result['content']}")
        click.echo("---")

if __name__ == '__main__':
    cli()