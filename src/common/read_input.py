from pathlib import Path

src_path = Path(__file__).parent.parent

# Reads input_file and returns the file contents in an array, split by line
def read_input(input_file_name='input.txt', year=2022, day=1):
    input = []
    
    input_file_path = src_path / str(year) / f'day{day}' / input_file_name
    with input_file_path.open() as f:
        input = f.read().splitlines()

    return input
