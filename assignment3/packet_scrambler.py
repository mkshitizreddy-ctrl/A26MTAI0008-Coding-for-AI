"""
Program: Multi-Dimensional Packet Scrambler
Purpose: Runs a data packet through a four-stage pipeline using only
         built-in list operations, no external libraries.
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

# Note: front_half, back_half, and scrambled are all built through
# slicing/concatenation, never direct assignment, so none of them alias
# packet. The id() check above confirms slicing returns a new list.
# Since Stage 3's mutations only run on scrambled, packet stays exactly
# as it was at Stage 1.


def scramble(data):
    """Stretch goal - same pipeline, returns result instead of printing."""
    mid = len(data) // 2
    front, back = data[:mid], data[mid:]
    result = back[::-1] + front

    mi = len(result) // 2
    if result and type(result[mi]) is int:
        result.insert(mi + 1, "SYNC-BIT")

    while 0 in result:
        result.remove(0)

    return result
