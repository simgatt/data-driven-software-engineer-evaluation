# Data-Driven Software Engineer Evaluation

## Workflow for Submission

1. **Fork this Repository**: please fork this repository to your own GitHub account to work independently
2. **Complete the Tasks**: clone your fork locally, complete the tasks, and commit your changes to your fork
3. When your work is complete, send the link to your repository to the following e-mail address: *softwarearchitect@minervadigitalintelligence.com*

## Deadline 

You have 48 hours from the time of receiving this link to submit your completed repository link via email.


-------

## Panoramica del Progetto
Questo progetto elabora file PDF per estrarre dati di testo e salvarli in un formato JSON strutturato. Progettato per essere scalabile ed efficiente, il sistema può gestire un elevato numero di file e include funzionalità di gestione degli errori e di logging.

### Struttura del Progetto
- **src**: Contiene lo script principale di elaborazione, `pdf_processor.py`, con le funzioni per l'estrazione del testo e la generazione del file JSON.
- **data-processing**: Cartella per i PDF di input e per il file JSON di output con i dati estratti.
- **tests**: Contiene gli script di test per verificare la funzionalità di estrazione e salvataggio.

### Requisiti
Assicurarsi di avere Python installato. Creare un ambiente virtuale e installare le dipendenze:

```bash
python -m venv venv
source venv/bin/activate  # Su Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Esecuzione del Progetto

Inserire i file PDF nella cartella data-processing/pdfs, quindi eseguire:
```bash
python src/pdf_processor.py
```
I dati estratti verranno salvati nel file data-processing/extracted_data.json.

### Logging

Il processo registra i passaggi di elaborazione, inclusi eventuali errori, nel file `src/process_log.log`.

### Test Automatizzati

Per verificare il funzionamento, eseguire i test automatizzati:
```bash
python -m unittest discover tests
```
I test includono verifiche per l'estrazione corretta del testo e la creazione del file JSON di output.