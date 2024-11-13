import pdfplumber
import json
import os

"""Estrae il testo dal singolo PDF e lo restituisce come stringa"""
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

"""Processa tutti i PDF nella cartella specificata e salva il testo in un file JSON"""
def process_pdfs(input_folder, output_file):
    data = {}
    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(input_folder, filename)
            try:
                text = extract_text_from_pdf(pdf_path)
                data[filename] = text
            except Exception as e:
                print(f"Errore durante l'elaborazione di {filename}: {e}")

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"Data extracted and saved to {output_file}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    input_folder = os.path.join(base_dir, "data-processing", "pdfs")
    output_file = os.path.join(base_dir, "data-processing", "extracted_data.json")

    process_pdfs(input_folder, output_file)
