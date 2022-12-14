# Advent of Code

This repo contains my Python solutions to the Advent of Code puzzles.

Puzzles can be found here: https://adventofcode.com/

## Adding New Days

You can add a new day by simply running the following command from the repo's root directory:

```
pipenv run python -m src.common.gen_starter_code 2021 1
```

Where you can replace the 2021 with the year and the 1 with the day.

## Running a Puzzle Solution

You can run a puzzle solution by running the following command:

```
pipenv run python -m src.2021.day1.puzzle1
```

Where you can replace the year, day, and puzzle number with the appropriate year (2015-2022), day (1 - 25), and puzzle number (1 - 2).

Note that it is required to run the python scripts using the module names instead of just the file name directly, as that is how the import statements are currently set up as. This also means that none of the python files can use `if __name__ == 'main':` as all scripts will be run as a module and not a mian executable.