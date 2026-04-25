# Image Phone Number Extractor

Extracts Brazilian phone numbers from images using OCR ([Tesseract](https://github.com/tesseract-ocr/tesseract)).

## Requirements

- Python 3.9+
- Tesseract OCR
- Pipenv

## Setup

### 1. Install Tesseract

**macOS:**

```bash
brew install tesseract
```

**Ubuntu/Debian:**

```bash
sudo apt-get install tesseract-ocr
```

**Windows:** Download the installer from the [Tesseract GitHub releases](https://github.com/tesseract-ocr/tesseract) page.

### 2. Install Python dependencies

```bash
pipenv install --dev
```

### 3. Configure environment

Copy the example env file and adjust if needed:

```bash
cp .env.example .env
```

```ini
INPUT_FOLDER=./data/input
OUTPUT_FILE=./data/output/extracted_phone_numbers.txt
```

### 4. Create data directories

```bash
mkdir -p data/input data/output
```

## Usage

Place images in `data/input`, then run:

```bash
# Without country code (default)
pipenv run python src/main.py

# With +55 country code
pipenv run python src/main.py --include-country-code
```

Extracted numbers are saved to `data/output/extracted_phone_numbers.txt`.

## Running Tests

```bash
pipenv run pytest
```

## Linting

```bash
pipenv run flake8 src
```

## Contributing

Create a new branch and submit a pull request.
