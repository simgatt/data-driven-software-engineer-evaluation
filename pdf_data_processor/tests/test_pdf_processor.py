import unittest
import os
import sys
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.pdf_processor import extract_text_from_pdf, process_pdfs

class TestPDFProcessor(unittest.TestCase):

    """Configura l'ambiente di test."""
    def setUp(self):
        self.test_pdf_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../data-processing/pdfs/sample-1.pdf"))
        self.test_output_json = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../data-processing/test_extracted_data.json"))

    """Ripulisce l'ambiente di test."""
    def tearDown(self):
        if os.path.exists(self.test_output_json):
            os.remove(self.test_output_json)

    """Testa l'estrazione di testo da un PDF."""
    def test_extract_text_from_pdf(self):
        text = extract_text_from_pdf(self.test_pdf_path)
        self.assertIsInstance(text, str)
        self.assertGreater(len(text), 0)

    """Testa il processo di estrazione e salvataggio dati in JSON."""
    def test_process_pdfs(self):
        input_folder = os.path.dirname(self.test_pdf_path)
        process_pdfs(input_folder, self.test_output_json)

        self.assertTrue(os.path.exists(self.test_output_json))

        with open(self.test_output_json, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.assertIn("sample-1.pdf", data)
            self.assertIsInstance(data["sample-1.pdf"], str)
            self.assertGreater(len(data["sample-1.pdf"]), 0)

if __name__ == "__main__":
    unittest.main()

