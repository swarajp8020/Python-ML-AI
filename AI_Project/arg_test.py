import sys

# sys.argv is a LIST of words typed in the terminal
print(f"Arguments received: {sys.argv}")

# The first argument (Index 0) is always the script name itself
print(f"Script Name: {sys.argv[0]}")

# The second argument (Index 1) is what you typed next
if len(sys.argv) > 1:
    print(f"Target File: {sys.argv[1]}")
else:
    print("You didn't provide a file name!")