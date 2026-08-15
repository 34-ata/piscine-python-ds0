import sys


def main():
    """Checks whether a given integer argument is odd or even."""
    if len(sys.argv) == 1:
        return
    assert len(sys.argv) <= 2, "more than one argument is provided"
    arg = sys.argv[1]
    assert (
        (arg.startswith("-") and arg[1:].isnumeric())
        or arg.isnumeric()
    ), "argument is not an integer"

    number = int(arg)
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
