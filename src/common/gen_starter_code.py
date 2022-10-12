from pathlib import Path
import sys
from string import Template

src_path = Path(__file__).parent.parent

# Reads day and generates the starter code for that day number


def gen_starter_code(day='1'):
    day_dir = f'day{day}'
    day_path = src_path / day_dir

    if day_path.exists() and day_path.is_dir():
        print(f'{day_path} already exists!')
        return

    print(f'Creating directory {day_path} ...')
    day_path.mkdir(parents=True, exist_ok=True)
    print(f'Created directory {day_path} !\n')

    init_file_name = '__init__.py'
    init_path = day_path / init_file_name
    print(f'Creating file {init_path} ...')
    with init_path.open('x') as f:
        pass
    print(f'Created file {init_path} !\n')

    for i in range(1, 3):
        input_i_file_name = f'input{i}.txt'
        input_i_path = day_path / input_i_file_name
        print(f'Creating file {input_i_path} ...')
        with input_i_path.open('x') as f:
            pass
        print(f'Created file {input_i_path} !\n')

        template_file_name = 'template_starter_code.py'
        template_path = src_path / 'common' / template_file_name
        template_string = ''
        with template_path.open() as f:
            template_string = Template(f.read())

        puzzle_i_file_name = f'puzzle{i}.py'
        puzzle_i_path = day_path / puzzle_i_file_name
        print(f'Creating file {puzzle_i_path} ...')
        with puzzle_i_path.open('w') as f:
            f.write(template_string.substitute(
                day_dir=day_dir, input_i_file_name=input_i_file_name))
        print(f'Created file {puzzle_i_path} !\n')


gen_starter_code(sys.argv[1])
