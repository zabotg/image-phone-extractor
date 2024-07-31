import argparse
import os
import logging
from dotenv import load_dotenv
from tqdm import tqdm
from utils import extract_phone_numbers_from_image, get_image_paths, save_phone_numbers_to_file

load_dotenv()

INPUT_FOLDER = os.getenv('INPUT_FOLDER', '../data/input')
OUTPUT_FILE = os.getenv('OUTPUT_FILE', '../data/output/extracted_phone_numbers.txt')

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract Brazilian phone numbers from images.")
    parser.add_argument('--include-country-code', action='store_true', help="Include the +55 country code in the extracted phone numbers.")
    args = parser.parse_args()

    input_folder = os.getenv('INPUT_FOLDER', './data/input')
    output_file = os.getenv('OUTPUT_FILE', './data/output/extracted_phone_numbers.txt')

    image_paths = get_image_paths(input_folder)
    all_phone_numbers = []

    for image_path in tqdm(image_paths, desc="Processing images"):
        phone_numbers = extract_phone_numbers_from_image(image_path, args.include_country_code)
        all_phone_numbers.extend(phone_numbers)

    save_phone_numbers_to_file(all_phone_numbers, output_file)

if __name__ == "__main__":
    main()