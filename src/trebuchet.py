import re
from helpers import relative, timer

CALIBRATE_SAMPLE = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

CALIBRATE_AGAIN_SAMPLE = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

DIGITS = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
DIGITS_WORDS = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


# Calibrate by summing the first and last digit on each line
@timer
def calibrate():
    calibration = 0

    def add_calibration(line):
        nonlocal calibration
        tens = ones = None
        for char in line:
            if char in DIGITS:
                tens = tens or char
                ones = char
        calibration += int(f"{tens}{ones}")

    each_line("trebuchet.txt", add_calibration)

    return calibration


# Calibrate by summing the first and last digit on each line,
# including numbers spelled out with letters e.g. one, two
@timer
def calibrate_again():
    calibration = 0

    def add_calibration(line):
        nonlocal calibration
        expr = re.compile("(?=([1-9]|one|two|three|four|five|six|seven|eight|nine))")
        matches = expr.findall(line)
        tens, ones = canonicalize(matches[0]), canonicalize(matches[-1])
        calibration += int(f"{tens}{ones}")

    each_line("trebuchet.txt", add_calibration)

    return calibration


def each_line(file, func):
    with open(relative(file), "r") as file:
        for line in file:
            func(line)


def canonicalize(digit):
    if digit in DIGITS:
        return digit
    return str(DIGITS_WORDS.index(digit))


if __name__ == "__main__":
    calibration = calibrate()
    calibration_again = calibrate_again()
