# Logic Trace: A Python for-loop is bounded by len() of the sequence it
# iterates over. When a batch is [], range(len(batch)) - or iterating the
# batch directly - has zero elements to step through, so the loop body
# never executes and control falls straight through to the next line.
# There is no manual counter or condition to get stuck on, unlike a
# C-style loop, so an empty batch simply does nothing and the audit moves
# on to the next batch.
#
# Author: Kshitiz

telemetry_stream = [
    [22.5, 23.0, 22.8],
    [25.1, "ERR", 24.9],
    [30.2, 35.5, 40.1],
    [22.0, 22.1, "STOP"],
]

shutdown_triggered = False

for batch_id in range(len(telemetry_stream)):
    batch = telemetry_stream[batch_id]
    previous_value = None
    print(f"--- Auditing Batch {batch_id}: {batch} ---")

    for reading in batch:
        if reading == "STOP":
            print(f"Emergency Shutdown at Batch {batch_id}.")
            shutdown_triggered = True
            break

        if reading == "ERR":
            print(f"Noise ignored at Batch {batch_id} (ERR).")
            continue

        if isinstance(reading, (int, float)):
            if reading > 35.0:
                print(f"Anomaly Detected at Batch {batch_id}: {reading}")

            if previous_value is not None:
                delta = abs(reading - previous_value)
                if delta > 5.0:
                    print(f"Spike Detected at Batch {batch_id}: "
                          f"{previous_value} -> {reading} (Delta {delta:.1f})")

            previous_value = reading

    if shutdown_triggered:
        break

else:
    print("Audit Complete: No system-wide failures")

# Submission Documentation:
# shutdown_triggered starts False and is only ever set True inside the
# inner loop, when a "STOP" reading is found. The inner loop's break just
# exits that batch's reading loop, so straight after it I check the flag
# and break the outer batch loop too, which is what actually stops the
# whole audit early. Because the outer for-loop's else clause only runs
# when the loop finishes without break, and the outer loop is only broken
# when shutdown_triggered is True, the else block prints "Audit Complete"
# in every run except the one where STOP was actually seen. If STOP never
# appears, shutdown_triggered stays False, the outer loop is never broken,
# and the else fires normally at the end.
