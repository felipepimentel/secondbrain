import os
from PIL import Image
import pytesseract
import docx2txt
import PyPDF2

def process_document(file_path):
    _, file_extension = os.path.splitext(file_path)
    
    if file_extension.lower() in ['.txt', '.md']:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    elif file_extension.lower() == '.docx':
        content = docx2txt.process(file_path)
    elif file_extension.lower() == '.pdf':
        content = extract_text_from_pdf(file_path)
    elif file_extension.lower() in ['.jpg', '.jpeg', '.png']:
        content = extract_text_from_image(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_extension}")

    return {
        'path': file_path,
        'content': content
    }

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        return ' '.join([page.extract_text() for page in reader.pages])

def extract_text_from_image(file_path):
    image = Image.open(file_path)
    return pytesseract.image_to_string(image)