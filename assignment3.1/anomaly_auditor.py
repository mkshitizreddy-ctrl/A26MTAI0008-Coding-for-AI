# Logic Trace: a for-loop is bounded by the length of what it iterates
# over. If a batch is [], there's nothing to loop through, so the body
# just never runs and we move to the next batch. No way for it to hang.
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

# Submission Note: shutdown_triggered starts False and only gets set to
# True when "STOP" shows up. break only exits the inner loop, so right
# after it I check the flag and break the outer loop too - that's what
# actually stops the audit. The outer else only runs if the outer loop
# wasn't broken, so it correctly skips "Audit Complete" whenever STOP
# was seen, and prints it normally otherwise.
