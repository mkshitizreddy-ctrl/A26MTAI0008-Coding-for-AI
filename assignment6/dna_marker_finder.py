# "Call by object reference" means the parameter name inside a function
# gets bound to the same object the caller's variable points to - not a
# copy (that's pass by value, like Java does with primitives) and not a
# pointer-to-a-pointer either (that's pass by reference, like C++ &args).
# It's just two names pointing at one object. If the function mutates
# that object (like .append()), the change shows up everywhere, because
# there was only ever one object. If the function reassigns the local
# name to something else, that only repoints the local name - the
# caller's variable still points at the original object.
#
# Author: Kshitiz


def search4letters(phrase: str, letters: str = 'ATCG') -> set:
    """Return the set of target letters found in a supplied phrase."""
    return set(letters).intersection(set(phrase))


def analyze_sequence(sequence_list, marker):
    print(f"Inside Function (Start) - ID: {id(sequence_list)} | "
          f"Data: {sequence_list}")
    sequence_list.append(marker)
    print(f"Inside Function (End) - ID: {id(sequence_list)} | "
          f"Data: {sequence_list}")


def analyze_sequence_rebind(sequence_list, marker):
    print(f"Inside (Start) - ID: {id(sequence_list)}")
    sequence_list = sequence_list + [marker]
    print(f"Inside (End) - ID: {id(sequence_list)} | Data: {sequence_list}")


# --- Task 1: search4letters ---
print("--- Task 1: search4letters ---")
print("Positional:", search4letters('TGGACC', 'GC'))
print("Keyword:", search4letters(letters='CG', phrase='TGGACC'))
print("Default markers:", search4letters('TGGACC'))

# --- Task 2: mutation demo ---
print()
print("--- Task 2: Mutation Demo ---")
dna_database = ['AATCCG', 'TGGCTA']
print(f"Global Scope (Before) - ID: {id(dna_database)} | Data: {dna_database}")
analyze_sequence(dna_database, 'CGAT')
print(f"Global Scope (After) - ID: {id(dna_database)} | Data: {dna_database}")

# --- Slice experiment ---
print()
print("--- Slice Experiment ---")
dna_database = ['AATCCG', 'TGGCTA']
print(f"Global Scope (Before) - ID: {id(dna_database)} | Data: {dna_database}")
analyze_sequence(dna_database[:], 'CGAT')
print(f"Global Scope (After) - ID: {id(dna_database)} | Data: {dna_database}")

# --- Bonus: rebind experiment ---
print()
print("--- Bonus: Rebind Experiment ---")
dna_database = ['AATCCG', 'TGGCTA']
print(f"Global Scope (Before) - ID: {id(dna_database)} | Data: {dna_database}")
analyze_sequence_rebind(dna_database, 'CGAT')
print(f"Global Scope (After) - ID: {id(dna_database)} | Data: {dna_database}")

# Submission Note (Discovery Challenge answer, written before checking
# the provided explanation): dna_database got modified even though
# analyze_sequence never returned anything because the function's
# parameter and the global variable point at the same list object - the
# function was never given a copy. .append() edits that object in place,
# so both names see the change, no return needed. My prediction matches
# the explanation given in the assignment.
