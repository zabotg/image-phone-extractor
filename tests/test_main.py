import os
import sys
import pytest
from utils import get_image_paths, save_phone_numbers_to_file

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


@pytest.fixture
def setup_test_env(tmp_path):
    test_input_folder = tmp_path / "input"
    test_output_folder = tmp_path / "output"
    test_input_folder.mkdir()
    test_output_folder.mkdir()
    return test_input_folder, test_output_folder


def test_get_image_paths(setup_test_env):
    test_input_folder, _ = setup_test_env
    (test_input_folder / "test_image1.jpg").touch()
    (test_input_folder / "test_image2.png").touch()

    image_paths = get_image_paths(test_input_folder)
    assert len(image_paths) == 2
    assert str(test_input_folder / "test_image1.jpg") in image_paths
    assert str(test_input_folder / "test_image2.png") in image_paths


def test_save_phone_numbers_to_file(setup_test_env):
    _, test_output_folder = setup_test_env
    test_output_file = test_output_folder / "output.txt"
    phone_numbers = ["11912345678", "21987654321"]

    save_phone_numbers_to_file(phone_numbers, test_output_file)
    with open(test_output_file, 'r') as file:
        lines = file.readlines()
    assert lines == ["11912345678\n", "21987654321\n"]


if __name__ == "__main__":
    pytest.main()
