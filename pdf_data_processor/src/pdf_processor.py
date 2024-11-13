import pdfplumber
import json
import os
import logging

logging.basicConfig(
    filename="process_log.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

"""Estrae il testo da un singolo PDF e lo restituisce come stringa."""
def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        logging.info(f"Successfully extracted text from {pdf_path}")
    except Exception as e:
        logging.error(f"Errore durante l'estrazione dal PDF {pdf_path}: {e}")
        raise
    return text

"""Processa tutti i PDF nella cartella specificata e salva il testo in un file JSON."""
def process_pdfs(input_folder, output_file):
    data = {}
    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(input_folder, filename)
            try:
                logging.info(f"Processing {filename}...")
                text = extract_text_from_pdf(pdf_path)
                data[filename] = text
            except Exception as e:
                logging.error(f"Errore durante l'elaborazione di {filename}: {e}")

    try:
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        logging.info(f"Data successfully saved to {output_file}")
    except Exception as e:
        logging.error(f"Errore durante il salvataggio del file JSON {output_file}: {e}")
        raise

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    input_folder = os.path.join(base_dir, "data-processing", "pdfs")
    output_file = os.path.join(base_dir, "data-processing", "extracted_data.json")

    logging.info("Inizio del processo di estrazione dati dai PDF")
    process_pdfs(input_folder, output_file)
    logging.info("Processo completato")
