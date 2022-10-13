from pathlib import Path
import sys
from string import Template

src_path = Path(__file__).parent.parent


def create_empty_file(file_path):
    print(f'Creating file {file_path} ...')
    with file_path.open('x') as f:
        pass
    print(f'Created file {file_path} !\n')


# Reads day and generates the starter code for that day number
def gen_starter_code(year='2022', day='1'):
    day_path = src_path / str(year) / f'day{day}'

    if day_path.exists() and day_path.is_dir():
        print(f'{day_path} already exists!')
        return

    print(f'Creating directory {day_path} ...')
    day_path.mkdir(parents=True, exist_ok=True)
    print(f'Created directory {day_path} !\n')

    create_empty_file(day_path / '__init__.py')
    create_empty_file(day_path / 'input.txt')
    create_empty_file(day_path / 'test.txt')

    for i in range(1, 3):
        template_file_name = 'template_starter_code.py'
        template_path = src_path / 'common' / template_file_name
        template_string = ''
        with template_path.open() as f:
            template_string = Template(f.read())

        puzzle_i_file_name = f'puzzle{i}.py'
        puzzle_i_path = day_path / puzzle_i_file_name
        print(f'Creating file {puzzle_i_path} ...')
        with puzzle_i_path.open('w') as f:
            f.write(template_string.substitute(year=year, day=day))
        print(f'Created file {puzzle_i_path} !\n')


year = sys.argv[1]
day = sys.argv[2]
gen_starter_code(year, day)
