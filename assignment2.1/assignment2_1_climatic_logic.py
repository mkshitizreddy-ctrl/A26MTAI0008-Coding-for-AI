"""
Program: Climatic Risk Intelligence Module
Purpose: Classifies a work-site into a safety tier (Freeze Alert, Critical,
         Cautionary, Operational) from a derived Heat Stress Index, using
         the walrus operator for input capture and short-circuit logic.
Author: Kshitiz

Heuristic Tiering Model: HSI = Temperature + (0.5 * Humidity). Freeze
Alert is checked first regardless of HSI, since a high-humidity freezing
site can still produce a numerically large HSI. Critical and Cautionary
are checked next in that order; Operational is the catch-all else, which
avoids an unnecessary explicit lower-bound condition.
"""

if (temp_str := input("Temperature (C): ").strip()):
    try:
        temperature = float(temp_str)
    except ValueError:
        temperature = None
else:
    temperature = None

if temperature is None:
    print("Safety Level: Unknown")
else:
    humidity_str = input("Humidity (%): ").strip()
    try:
        humidity = float(humidity_str)
        assert humidity >= 0, "Telemetry Error: Negative Humidity"
    except ValueError:
        humidity = None

    if humidity is None:
        print("Safety Level: Unknown")
    else:
        hsi = temperature + (0.5 * humidity)

        if temperature <= 0:
            tier = "FREEZE ALERT"
        elif hsi > 45 or (temperature > 38 and humidity > 70):
            tier = "CRITICAL"
        elif 30 <= hsi <= 45:
            wind_str = input("Wind speed (km/h): ").strip()
            wind_speed = float(wind_str) if wind_str else 0.0
            tier = "CAUTIONARY" if wind_speed < 5 else "OPERATIONAL"
        else:
            tier = "OPERATIONAL"

        # Challenge Task: Nested Intelligence Suite (battery adjustment)
        if tier == "CAUTIONARY":
            battery_str = input("Battery level (%): ").strip()
            battery = float(battery_str) if battery_str else 100.0
            if battery < 20:
                tier = "CRITICAL"
            elif battery > 80:
                tier = "OPERATIONAL"

        risk_label = "Safe" if hsi < 30 else "Unsafe"
        print(f"HSI: {hsi:.1f}")
        print(f"Safety Level: {tier}")
        print(f"Risk Label: {risk_label}")
