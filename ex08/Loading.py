import os


def ft_tqdm(lst: range) -> None:
    """Mimics tqdm's progress bar behavior using yield."""
    total = len(lst)
    terminal_width = os.get_terminal_size().columns
    bar_length = terminal_width - 30
    for i, elem in enumerate(lst):
        percent = (i + 1) / total
        filled = int(bar_length * percent)
        bar = "=" * filled + ">" + " " * (bar_length - filled - 1)
        print(f"{int(percent * 100)}%|{bar}| {i + 1}/{total}", end="\r",
              flush=True)
        yield elem
