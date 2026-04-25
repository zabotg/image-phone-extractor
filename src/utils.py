import logging
import os
import re
from typing import List

import pytesseract
from PIL import Image

logger = logging.getLogger(__name__)

VALID_IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')

_PHONE_PATTERN_WITH_COUNTRY = re.compile(r'(\+55)?\s*(\d{2})\s*(\d{4,5})[-.\s]?(\d{4})')
_PHONE_PATTERN_WITHOUT_COUNTRY = re.compile(r'(\d{2})\s(\d{4,5})-(\d{4})')


def extract_phone_numbers_from_image(image_path: str, include_country_code: bool = False) -> List[str]:
    pattern = _PHONE_PATTERN_WITH_COUNTRY if include_country_code else _PHONE_PATTERN_WITHOUT_COUNTRY
    try:
        text = pytesseract.image_to_string(Image.open(image_path))
        return [''.join(match) for match in pattern.findall(text)]
    except Exception as e:
        logger.error("Error processing image %s: %s", image_path, e)
        return []


def get_image_paths(folder_path: str) -> List[str]:
    return [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if f.lower().endswith(VALID_IMAGE_EXTENSIONS)
    ]


def save_phone_numbers_to_file(phone_numbers: List[str], file_path: str) -> None:
    output_dir = os.path.dirname(file_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    try:
        with open(file_path, 'w') as file:
            file.writelines(f"{number}\n" for number in phone_numbers)
        logger.info("Phone numbers saved to %s", file_path)
    except Exception as e:
        logger.error("Error writing to file %s: %s", file_path, e)
