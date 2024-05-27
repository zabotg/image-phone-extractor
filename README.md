# Image Phone Number Extractor

This project extracts Brazilian phone numbers from images using OCR (Optical Character Recognition) with [Tesseract](https://github.com/tesseract-ocr/tesseract).

## Requirements

- Python 3.9+
- Pipenv

## Setup

1. Install dependencies:

    ```bash
    pipenv install --dev
    ```

2. Create and configure the `.env` file:

    ```ini
    INPUT_FOLDER=./data/input
    OUTPUT_FILE=./data/output/extracted_phone_numbers.txt
    ```

3. Create the input and output directories:

    ```bash
    mkdir -p data/input
    mkdir -p data/output
    ```

## Usage

1. Place the images from which you want to extract phone numbers in the `data/input` directory.

2. Run the script:

    ```bash
    pipenv run python src/main.py
    ```

3. Extracted phone numbers will be saved to `data/output/extracted_phone_numbers.txt`.

## Linting

To check the code for linting errors using `flake8`, run:

```bash
pipenv run flake8 src
```# image-phone-extractor
