import sys
import google.generativeai as genai
from config import GEMINI_API_KEY

# 1. SETUP AI
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-flash-latest')

# 2. CHECK ARGUMENTS (New Logic!)
if len(sys.argv) < 2:
    print("Error: You must provide a file name.")
    print("Usage: python code_reviewer.py <filename>")
    sys.exit()

# Get the filename from the command line
target_file = sys.argv[1]

# 3. READ THE FILE (Dynamic!)
print(f"--- Reading {target_file} ---")
try:
    with open(target_file, "r") as f:
        code_content = f.read()
except FileNotFoundError:
    print("Error: File not found. Check your spelling!")
    sys.exit()

# 4. SEND TO AI
prompt = f"Fix this python code and return ONLY code:\n{code_content}"
print("--- Sending to AI ---")
response = model.generate_content(prompt)

# 5. SAVE THE FIX
output_name = f"fixed_{target_file}" # e.g., fixed_buggy_code.py
print(f"--- Saving to {output_name} ---")

with open(output_name, "w") as f:
    f.write(response.text)

print("Done. Happy Coding!")