import weaviate

class WeaviateClient:
    def __init__(self, url):
        self.client = weaviate.Client(url)
        self.setup_schema()

    def setup_schema(self):
        schema = {
            "class": "Document",
            "properties": [
                {"name": "path", "dataType": ["string"]},
                {"name": "content", "dataType": ["text"]}
            ]
        }
        self.client.schema.create_class(schema)

    def index_document(self, document):
        self.client.data_object.create(
            data_object=document,
            class_name="Document"
        )

    def delete_document(self, file_path):
        query = {
            "class": "Document",
            "where": {
                "path": ["==", file_path]
            }
        }
        self.client.data_object.delete(query)

    def search(self, query):
        return (
            self.client.query
            .get("Document", ["path", "content"])
            .with_near_text({"concepts": [query]})
            .with_limit(5)
            .do()
        )