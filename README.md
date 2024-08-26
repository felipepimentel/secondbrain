# SecondBrain

SecondBrain is an intelligent document management system that allows users to synchronize folders, index various file types, and perform semantic searches using natural language queries.

## Features

- Folder synchronization
- Document indexing (supports .txt, .md, .docx, .pdf, and image files)
- Semantic search using Weaviate vector database
- REST API for external integrations
- Command-line interface for easy management

## Quick Start with Docker

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/secondbrain.git
   cd secondbrain
   ```

2. Create a `.env` file in the project root with the following content:
   ```
   WEAVIATE_URL=http://weaviate:8080
   ```

3. Build and start the services using Docker Compose:
   ```
   docker compose up -d
   ```

   This will start both the SecondBrain application and the Weaviate database.

4. Access the API documentation at `http://localhost:8000/docs`

## Usage

### REST API

Use the following endpoints:
- POST `/search`: Perform a semantic search
- POST `/index`: Manually index a document
- DELETE `/document`: Delete a document from the index

### Command-line Interface (inside the Docker container)

1. Access the SecondBrain container:
   ```
   docker-compose exec secondbrain bash
   ```

2. Start folder synchronization:
   ```
   python -m secondbrain.cli sync /path/to/your/folder
   ```

3. Perform a search:
   ```
   python -m secondbrain.cli search "your search query"
   ```

## Development Setup

For local development without Docker:

1. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Install Tesseract OCR for image processing:
   - On Ubuntu: `sudo apt-get install tesseract-ocr`
   - On macOS: `brew install tesseract`
   - On Windows: Download and install from [GitHub](https://github.com/UB-Mannheim/tesseract/wiki)

4. Start the FastAPI server:
   ```
   uvicorn secondbrain.api:app --reload
   ```

## Configuration

You can modify the `config/config.yaml` file to customize various settings, such as:
- Supported file types
- Maximum file size for indexing
- Search result limit

## Running Tests

To run the test suite:
```
pytest tests/
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

SecondBrain is licensed under the [MIT License](LICENSE).