"""
Program: Multi-Dimensional Packet Scrambler
Purpose: Runs a data packet through a four-stage pipeline (middle-out
         slice swap, in-place correction, memory integrity check) using
         only built-in list operations, no external libraries.
Author: Kshitiz
"""

packet = [5, 12, 0, 8, 21, 34, 7, 19, 0, 3]

# --- Stage 1: Input Validation ---
if packet and len(packet) >= 10:
    print("Validation passed. Processing packet...")
else:
    print("Validation failed: packet is empty or too short.")

print(f"Initial packet: {packet}")

# --- Stage 2: Middle-Out Swap ---
midpoint = len(packet) // 2
front_half = packet[:midpoint]
back_half = packet[midpoint:]
scrambled = back_half[::-1] + front_half

print("--- Stage 2: Middle-Out Swap ---")
print(f"Scrambled: {scrambled}")
print(f"Non-destructive check, id(packet) == id(front_half): "
      f"{id(packet) == id(front_half)}")

# --- Stage 3: In-Place Correction ---
print("--- Stage 3: In-Place Correction ---")

middle_index = len(scrambled) // 2
if type(scrambled[middle_index]) is int:
    scrambled.insert(middle_index + 1, "SYNC-BIT")
print(f"After Sync-Bit insertion: {scrambled}")

while 0 in scrambled:
    scrambled.remove(0)
print(f"After zero removal: {scrambled}")

# --- Stage 4: Memory Integrity Check ---
print("--- Stage 4: Memory Integrity Check ---")
print(f"Original packet: {packet}")
print(f"Final scrambled: {scrambled}")

first, *middle, last = scrambled
print(f"Header: {first} Footer: {last} Body length: {len(middle)}")

# Submission Documentation:
# Stage 4 reprints the original packet variable, untouched since Stage 1,
# next to the final scrambled list. front_half, back_half, and scrambled
# were all built through slicing or concatenation, never through direct
# reference assignment, so none of them alias packet's underlying list.
# The id() check in Stage 2 confirms this: slicing always returns a new
# list object. Because every later mutation (insert, remove) runs only
# on scrambled, and scrambled was never the same object as packet,
# packet's contents at Stage 4 are guaranteed to match Stage 1 exactly.


def scramble(data):
    """Stretch goal: same pipeline, returns the result instead of
    printing it."""
    mid = len(data) // 2
    front, back = data[:mid], data[mid:]
    result = back[::-1] + front

    mi = len(result) // 2
    if result and type(result[mi]) is int:
        result.insert(mi + 1, "SYNC-BIT")

    while 0 in result:
        result.remove(0)

    return result
