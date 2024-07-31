import os
import re
from typing import List
import pytesseract
from PIL import Image


def extract_phone_numbers_from_image(image_path: str, include_country_code: bool) -> List[str]:
    """Extracts Brazilian phone numbers from an image.

    Args:
        image_path (str): The path to the image file.
        include_country_code (bool): Whether to include the +55 country code in the extracted phone numbers.

    Returns:
        List[str]: A list of extracted phone numbers.
    """
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        
        if include_country_code:
            pattern = re.compile(r'(\+55)?\s*(\d{2})\s*(\d{4,5})[-.\s]?(\d{4})')
        else:
            pattern = re.compile(r'(\d{2})\s(\d{4,5})-(\d{4})')

        matches = pattern.findall(text)
        return [''.join(match) for match in matches]
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        return []


def get_image_paths(folder_path: str) -> List[str]:
    """Gets the paths of all valid images in a folder.

    Args:
        folder_path (str): The path to the folder containing images.

    Returns:
        List[str]: A list of image file paths.
    """
    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')
    return [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.lower().endswith(valid_extensions)]


def save_phone_numbers_to_file(phone_numbers: List[str], file_path: str) -> None:
    """Saves extracted phone numbers to a text file.

    Args:
        phone_numbers (List[str]): A list of phone numbers to save.
        file_path (str): The path to the file where phone numbers will be saved.
    """
    try:
        with open(file_path, 'w') as file:
            for number in phone_numbers:
                file.write(f"{number}\n")
        print(f"Phone numbers saved to {file_path}")
    except Exception as e:
        print(f"Error writing to file {file_path}: {e}")
