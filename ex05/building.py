import string
import sys


def print_report(text, upper, lower, punct, space, digit):
    """Prints a report of character categories in a text."""
    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")


def count_chars(text):
    """Counts uppercase, lowercase, punctuation, spaces and digits in a
    text."""

    upper = 0
    lower = 0
    punct = 0
    space = 0
    digit = 0

    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isspace():
            space += 1
        elif char.isdigit():
            digit += 1
        elif char in string.punctuation:
            punct += 1

    return upper, lower, punct, space, digit


def main():
    """Counts uppercase, lowercase, punctuation, spaces and digits in a
    text."""
    assert len(sys.argv) <= 2, "the arguments are bad"
    if len(sys.argv) == 2:
        text = sys.argv[1]
    else:
        print("What is the text to count?")
        text = sys.stdin.read()
    print_report(text, *count_chars(text))


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
