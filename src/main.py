import os
import logging
from dotenv import load_dotenv
from tqdm import tqdm
from utils import extract_phone_numbers_from_image, get_image_paths, save_phone_numbers_to_file

load_dotenv()

INPUT_FOLDER = os.getenv('INPUT_FOLDER', './data/input')
OUTPUT_FILE = os.getenv('OUTPUT_FILE', './data/output/extracted_phone_numbers.txt')

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def process_images(input_folder, output_file):
    image_paths = get_image_paths(input_folder)
    all_phone_numbers = []

    for path in tqdm(image_paths, desc="Processing images"):
        phone_numbers = extract_phone_numbers_from_image(path)
        all_phone_numbers.extend(phone_numbers)

    if all_phone_numbers:
        save_phone_numbers_to_file(all_phone_numbers, output_file)
    else:
        logging.info("No phone numbers found.")


def main():
    logging.info("Starting the phone number extraction process...")
    process_images(INPUT_FOLDER, OUTPUT_FILE)
    logging.info("Phone number extraction process completed.")


if __name__ == "__main__":
    main()
