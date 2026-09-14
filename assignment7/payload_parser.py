# The / in a signature marks everything before it as positional-only -
# callers can't use those parameter names as keywords, only position.
# The * marks everything after it as keyword-only - callers must name
# those parameters, position won't work. Together they let an author
# lock down exactly how each parameter can be supplied, which matters
# for API stability (positional-only names can be renamed later without
# breaking callers) and safety (keyword-only args can't be swapped by
# accident if two same-typed parameters sit next to each other).
#
# Slicing inside the comprehension (raw_packet[1][:]) is enough to avoid
# aliasing because a slice always builds a brand-new list object holding
# the same values - it never just points back at the original list. The
# comprehension itself also builds a new list for its result, so nothing
# in the return value shares identity with raw_packet[1].
#
# Author: Kshitiz


def parse_payload(raw_packet: list, delimiter: str, /, *,
                   correction_offset: int = 0) -> tuple:
    status_tokens = raw_packet[2].split(delimiter)
    corrected_sensors = [
        value if "ERROR" in status_tokens else value + correction_offset
        for value in raw_packet[1][:]
    ]
    return raw_packet[0], corrected_sensors


# --- Test 1: normal correction ---
packet1 = [501, [12.5, 13.0, 11.8], "NOMINAL|CALIBRATED"]
original1 = packet1[1][:]
result1 = parse_payload(packet1, "|", correction_offset=2)
print(f"Test 1 -> {result1[0]} {result1[1]}")
assert packet1[1] == original1
assert id(result1[1]) != id(packet1[1])
print("Test 1 side-effect assertions passed.")

# --- Test 2: ERROR code suppresses the correction ---
packet2 = [502, [9.0, 8.5], "ERROR|SENSOR_FAULT"]
original2 = packet2[1][:]
result2 = parse_payload(packet2, "|", correction_offset=5)
print(f"Test 2 -> {result2[0]} {result2[1]}")
assert packet2[1] == original2
assert id(result2[1]) != id(packet2[1])
print("Test 2 side-effect assertions passed.")

# --- Test 3: default offset ---
packet3 = [503, [1.0, 2.0], "NOMINAL"]
result3 = parse_payload(packet3, "|")
print(f"Test 3 (default offset) -> {result3[0]} {result3[1]}")

# --- Test 4: illegal keyword call on positional-only params ---
try:
    parse_payload(raw_packet=packet1, delimiter="|")
except TypeError as e:
    print(f"Test 4 passed. TypeError raised as expected: {e}")

# --- Test 5: illegal positional call on keyword-only param ---
try:
    parse_payload(packet1, "|", 2)
except TypeError as e:
    print(f"Test 5 passed. TypeError raised as expected: {e}")

# Submission Note: Test 4 called parse_payload with raw_packet and
# delimiter as keywords, which isn't allowed since both sit before the
# / in the signature. Python raised "parse_payload() got some
# positional-only arguments passed as keyword arguments: 'raw_packet,
# delimiter'". Test 5 tried to pass correction_offset positionally as
# a third argument, which isn't allowed since it sits after the *.
# Python raised "parse_payload() takes 2 positional arguments but 3
# were given". Both matched what the assignment predicted.
