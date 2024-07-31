# Image Phone Number Extractor

This project extracts Brazilian phone numbers from images using OCR (Optical Character Recognition) with [Tesseract](https://github.com/tesseract-ocr/tesseract).

## Requirements

- Python 3.9+
- Tesseract
- Pipenv

## Setup

1. Install Tesseract:

   On macOS, you can install Tesseract using Homebrew:

    ```bash
    brew install tesseract
    ```

    On Ubuntu/Debian, use:

    ```bash
    sudo apt-get update
    sudo apt-get install tesseract-ocr
    ```

    On Windows, download the installer from the [Tesseract GitHub releases](https://github.com/tesseract-ocr/tesseract) page and follow the installation instructions.

2. Install dependencies:
   Navigate to the project directory and run:

    ```bash
    pipenv install --dev
    ```

3. Create and configure the `.env` file:
   Create a .env file in the root of your project with the following content:

    ```ini
    INPUT_FOLDER=./data/input
    OUTPUT_FILE=./data/output/extracted_phone_numbers.txt
    ```

4. Create the input and output directories:

    ```bash
    mkdir -p data/input
    mkdir -p data/output
    ```

## Usage

1. Place the images from which you want to extract phone numbers in the `data/input` directory.

2. Run the script with the appropriate options:

    - With Country Code (+55):

    ```bash
    python src/main.py --include-country-code
    ```

    - Without Country Code:

    ```bash
    pipenv run python src/main.py
    ```

3. Extracted phone numbers will be saved to `data/output/extracted_phone_numbers.txt`.

## Linting

To check the code for linting errors using `flake8`, run:

```bash
pipenv run flake8 src
```

Contributing
If you'd like to contribute, please create a new branch, and submit a pull request.
