def search4letters(phrase: str, letters: str = 'ATCG') -> set:
    """Return the set of target letters found in a supplied phrase, matching every marker character present."""
    return set(letters).intersection(set(phrase))


def another_function():
    pass
