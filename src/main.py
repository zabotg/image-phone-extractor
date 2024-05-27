import os
import re
import pytesseract
from PIL import Image
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv()

INPUT_FOLDER = os.getenv('INPUT_FOLDER', './data/input')
OUTPUT_FILE = os.getenv('OUTPUT_FILE', './data/output/extracted_phone_numbers.txt')


def extract_phone_numbers_from_image(image_path):
    """
    Extracts phone numbers from a given image.

    Args:
    image_path (str): The path to the image file.

    Returns:
    list: A list of extracted phone numbers without the "+55" prefix.
    """
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
    """
    Retrieves all image file paths from the specified folder.

    Args:
    folder_path (str): The path to the folder containing image files.

    Returns:
    list: A list of image file paths.
    """
    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')
    return [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.lower().endswith(valid_extensions)]


def save_phone_numbers_to_file(phone_numbers, file_path):
    """
    Saves extracted phone numbers to a file.

    Args:
    phone_numbers (list): The list of extracted phone numbers.
    file_path (str): The path to the output file.
    """
    try:
        with open(file_path, 'w') as file:
            for number in phone_numbers:
                file.write(f"{number}\n")
        print(f"Phone numbers saved to {file_path}")
    except Exception as e:
        print(f"Error writing to file {file_path}: {e}")


def main():
    image_paths = get_image_paths(INPUT_FOLDER)
    all_phone_numbers = []

    for path in tqdm(image_paths, desc="Processing images"):
        phone_numbers = extract_phone_numbers_from_image(path)
        all_phone_numbers.extend(phone_numbers)

    if all_phone_numbers:
        save_phone_numbers_to_file(all_phone_numbers, OUTPUT_FILE)
    else:
        print("No phone numbers found.")


if __name__ == "__main__":
    main()
