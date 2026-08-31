# For a batch of length batch_length (ID at index 0), i counts up from
# 1 to batch_length - 1, and target_index = batch_length - i maps that
# to a right-to-left position. At i=1, target_index is the last index;
# as i grows it shrinks down to 1, the first reading after the ID.
#
# The while loop stops on its own because slicing past the end of a
# list just returns [] instead of erroring. Once feed_cursor passes the
# last index, the one-item slice is empty (falsy), and the loop ends -
# no separate length check needed.
#
# Author: Kshitiz

calibration_feed = [
    [201, 6.0, 9.5, "IGNORE", 4.0],
    [],
    [202, 11.2, "FAULT", 7.8, 5.5],
    [203, 14.0, 3.5, 8.25],
    [204, 2.75, "HALT", 6.0],
]

feed_cursor = 0
total_valid_readings = 0
global_max = None
global_min = None
checksum = 0.0
emergency_stop = False

while (current_slice := calibration_feed[feed_cursor:feed_cursor + 1]):
    batch = current_slice[0]

    if not batch:
        print(f"Batch {feed_cursor} is EMPTY. Proceeding.")
        feed_cursor += 1
        continue

    calibration_id = batch[0]
    print(f"Evaluating Batch {feed_cursor} (ID: {calibration_id})...")

    # Manual length count (no len()).
    batch_length = 0
    for _ in batch:
        batch_length += 1

    batch_sum = 0.0

    for i in range(1, batch_length):
        target_index = batch_length - i
        reading = batch[target_index]

        if reading == "IGNORE":
            print(f"Signal IGNORE encountered at Batch {calibration_id}.")
            continue

        if reading == "FAULT":
            print(f"Signal FAULT detected. Suppressing batch {calibration_id}.")
            break

        if reading == "HALT":
            print("Signal HALT detected. Executing emergency protocol.")
            emergency_stop = True
            break

        batch_sum += reading
        total_valid_readings += 1

        if global_max is None or reading > global_max:
            global_max = reading
        if global_min is None or reading < global_min:
            global_min = reading

    else:
        if calibration_id % 2 == 0:
            batch_sum *= 1.5
        else:
            batch_sum *= 0.8
        checksum += batch_sum

    if emergency_stop:
        break

    feed_cursor += 1

print()
print("=" * 40)
if emergency_stop:
    print("CALIBRATION COMPLETE: EMERGENCY TERMINATION")
else:
    print("CALIBRATION COMPLETE: FULL FEED PROCESSED")
print("=" * 40)
print(f"Total Valid Readings Processed: {total_valid_readings}")
print(f"Global Calibration Checksum: {round(checksum, 2)}")
print(f"Maximum Reading Encountered: {global_max}")
print(f"Minimum Reading Encountered: {global_min}")

# Submission Note: Batch 2 (FAULT) and Batch 4 (HALT) both had their
# else block skipped since break was hit in the inner loop - their
# valid readings still count toward the total, but their sums never
# reach the checksum. Batches 0 and 3 finished without breaking, so
# their else blocks ran and got added to the checksum.
