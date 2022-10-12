from pathlib import Path

src_path = Path(__file__).parent.parent

# Reads input_file and returns the file contents in an array, split by line
def read_input(input_file_name='input.txt'):
    input = []
    
    input_file_path = src_path / input_file_name
    with input_file_path.open() as f:
        input = f.read().splitlines()

    return input
