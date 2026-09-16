def search4letters(phrase:str, letters: str = 'ATCG') -> set:
    """Return the set of target letters found in a supplied phrase."""    
    return set(letters).intersection(set(phrase))
def another_function():
    pass
