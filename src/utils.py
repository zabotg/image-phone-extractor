import os
import re
import pytesseract
from PIL import Image


def extract_phone_numbers_from_image(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        pattern = re.compile(r'\+55\s(\d{2})\s(\d{4,5})-(\d{4})')
        matches = pattern.findall(text)
        return [''.join(match) for match in matches]
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        return []


def get_image_paths(folder_path):
    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')
    return [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.lower().endswith(valid_extensions)]


def save_phone_numbers_to_file(phone_numbers, file_path):
    try:
        with open(file_path, 'w') as file:
            for number in phone_numbers:
                file.write(f"{number}\n")
        print(f"Phone numbers saved to {file_path}")
    except Exception as e:
        print(f"Error writing to file {file_path}: {e}")
