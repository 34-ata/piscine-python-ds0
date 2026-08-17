import sys


NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ",
    "E": ". ", "F": "..-. ", "G": "--. ", "H": ".... ",
    "I": ".. ", "J": ".--- ", "K": "-.- ", "L": ".-.. ",
    "M": "-- ", "N": "-. ", "O": "--- ", "P": ".--. ",
    "Q": "--.- ", "R": ".-. ", "S": "... ", "T": "- ",
    "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ",
    "Y": "-.-- ", "Z": "--.. ",
    "0": "----- ", "1": ".---- ", "2": "..--- ", "3": "...-- ",
    "4": "....- ", "5": "..... ", "6": "-.... ", "7": "--... ",
    "8": "---.. ", "9": "----. "
}


def translate_morse():
    """Translates the command line argument into Morse code and prints it."""
    result = ""
    for x in sys.argv[1].upper():
        result += NESTED_MORSE[x]
    print(result.strip())


def check_string():
    """Checks whether the argument contains only letters, digits or spaces."""
    for x in sys.argv[1]:
        if not (x.isdigit() or x.isalpha() or x.isspace()):
            return False
    return True


def main():
    """Validates arguments and prints their Morse code translation."""
    assert len(sys.argv) == 2 and check_string(), "the arguments are bad"
    translate_morse()


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
