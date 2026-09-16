"""vsearch: text search tools for AI pre-processing.

Packaged with setup.py (py_modules=['vsearch']), built via
`python3 -m build --sdist`, and installed with pip so it can be
imported from anywhere, not just this folder. Passes pycodestyle
clean (see linting/ for the before/after run).

Author: Kshitiz
"""


def search4letters(phrase: str, letters: str = 'ATCG') -> set:
    """Return the set of target letters found in a supplied phrase."""
    return set(letters).intersection(set(phrase))
