"""
Program: Temporal Profile Analyzer
Purpose: Computes an AI Era Readiness Score from a name and age.
Author: Kshitiz
"""

import datetime

SINGULARITY_YEAR = 2045

# --- Name Analysis ---
user_full_name = input("Enter your full name: ").strip()

if not user_full_name:
    print("Input Error: Name cannot be empty or whitespace-only.")
else:
    name_length = len(user_full_name)
    formatted_name = user_full_name.title()
    print(f"Identifier Byte-Count: {name_length}")
    print(f"Formatted Name: {formatted_name}")

    # --- Temporal Projection ---
    age_input = input("Enter your current age: ").strip()

    if not age_input.isdigit():
        print("Input Error: Age must be a valid non-negative whole number.")
    else:
        current_age = int(age_input)
        current_year = datetime.date.today().year
        age_in_2045 = current_age + (SINGULARITY_YEAR - current_year)
        print(f"Current Year: {current_year}")
        print(f"Projected Age in {SINGULARITY_YEAR}: {age_in_2045}")

        # --- AI Readiness Formula ---
        score = ((name_length * 10) + age_in_2045) / 2
        print(f"AI Era Readiness Score: {score:.2f}")

        # Bonus: repeat name by age's leading digit.
        # age // 10 gives 0 for single-digit ages, so just use age then.
        if current_age >= 10:
            repeat_count = current_age // 10
        else:
            repeat_count = current_age

        repeated_name = formatted_name * repeat_count
        print(f"Bonus - Repeated Name ({repeat_count}x): {repeated_name}")
