from secondbrain.weaviate_client import WeaviateClient

class SearchEngine:
    def __init__(self, weaviate_client):
        self.weaviate_client = weaviate_client

    def search(self, query):
        results = self.weaviate_client.search(query)
        return self.process_results(results)

    def process_results(self, results):
        processed_results = []
        for result in results['data']['Get']['Document']:
            processed_results.append({
                'path': result['path'],
                'content': result['content'][:200] + '...'  # Truncate content for brevity
            })
        return processed_results