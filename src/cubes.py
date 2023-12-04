import re
import operator
from functools import reduce
from helpers import each_line, timer

RECORDS = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

LIMIT = {"red": 12, "green": 13, "blue": 14}


@timer
def sum_possible():
    possible = 0
    game_expr = re.compile(r"Game (\d+): (.*)$")
    set_expr = re.compile(r"(\d+) (red|green|blue)")

    def add_possible(line):
        nonlocal possible, game_expr, set_expr
        id, sets = game_expr.match(line).groups()
        for set in sets.split(";"):
            items = set_expr.findall(set)
            for count, color in items:
                if LIMIT[color] < int(count):
                    return
        possible += int(id)

    each_line("cubes.txt", add_possible)

    return possible


@timer
def sum_powers():
    powers = 0
    game_expr = re.compile(r"Game (\d+): (.*)$")
    set_expr = re.compile(r"(\d+) (red|green|blue)")

    def add_powers(line):
        nonlocal powers, game_expr, set_expr
        _, sets = game_expr.match(line).groups()
        min = {"red": 0, "green": 0, "blue": 0}
        for set in sets.split(";"):
            items = set_expr.findall(set)
            for count, color in items:
                int_count = int(count)
                if min[color] < int_count:
                    min[color] = int_count
        powers += reduce(operator.mul, min.values(), 1)

    each_line("cubes.txt", add_powers)

    return powers


if __name__ == "__main__":
    sum_possible()
    sum_powers()
