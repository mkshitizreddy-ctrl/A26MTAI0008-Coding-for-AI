# Raw text needs normalising before counting because Python compares
# strings exactly - "AI", "ai", and "AI," are three different keys to a
# dict even though they're the same word to a person. Lowercasing and
# stripping punctuation collapses all of those into one key.
#
# set_a - set_b only gives what's unique to A; set_a ^ set_b gives
# everything unique to either side combined, without saying which side
# it came from. Use the minus version when you need to know which
# platform a follower belongs to, and ^ when you just want the total
# "not on both" group.
#
# Author: Kshitiz

import string

# --- Task 1: Word Frequency Counter ---
text = ("AI is changing the world. ai is powering new tools, and AI is "
        "helping researchers learn faster. The world loves AI, and the "
        "world depends on it more each year.")

word_counts = {}
for raw_word in text.split():
    cleaned_word = raw_word.lower().strip(string.punctuation)
    if not cleaned_word:
        continue
    word_counts.setdefault(cleaned_word, 0)
    word_counts[cleaned_word] += 1

print("--- Word Frequency Counter ---")
print(word_counts)

# --- Task 2: Follower Deduplicator ---
platform_a_followers = ["u101", "u102", "u103", "u104", "u105"]
platform_b_followers = ["u103", "u104", "u106", "u107"]

set_a = set(platform_a_followers)
set_b = set(platform_b_followers)

both_platforms = set_a & set_b
only_a = set_a - set_b
only_b = set_b - set_a
either_only = set_a ^ set_b

print()
print("--- Follower Deduplicator ---")
print(f"Follows on both platforms: {both_platforms}")
print(f"Unique to Platform A: {only_a}")
print(f"Unique to Platform B: {only_b}")
print(f"Unique to exactly one platform: {either_only}")

# Submission Note: for the sample paragraph, "ai" comes out to 4 (AI, ai,
# AI, AI - the trailing comma and period get stripped) and "is"/"the"/
# "world" each come to 3, matching a manual word-by-word count of the
# text. For the follower lists, u103 and u104 show up on both platforms,
# u101/u102/u105 are only on A, and u106/u107 are only on B - the
# symmetric difference is just those last two groups combined, which
# checks out against adding only_a and only_b together by hand.
