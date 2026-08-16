import sys
from ft_filter import ft_filter


def main():
    """Filters words in a string longer than a given length."""
    assert len(sys.argv) == 3 and sys.argv[2].isnumeric(), \
        "the arguments are bad"
    words = sys.argv[1].split()
    n = int(sys.argv[2])
    print(ft_filter(lambda word: len(word) > n, words))


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
