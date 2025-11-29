# Challenge 3: The "Word Frequency" Data:
# words = ["ai", "python", "java", "ai", "java", "ai", "cloud"]
# Task: Create an empty Dictionary counts = {}.
# Loop through words.
# Check:
# If the word is NOT in counts, add it and set value to 1.
# If the word IS in counts, increase value by 1 (counts[word] += 1).

words = ["ai", "python", "java", "ai", "java", "ai", "cloud"]
counts = {}  # The empty floor (no buckets yet)

for word in words:
    # Check if the bucket ALREADY exists on the floor
    if word in counts:
        # YES: Just add a ball (increment count)
        counts[word] += 1
    else:
        # NO: Create the bucket and put the first ball in
        counts[word] = 1

print(counts)