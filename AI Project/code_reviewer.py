import google.generativeai as genai
from config import GEMINI_API_KEY

# 1. Configure AI
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-flash-latest')

# 2. Read the Buggy File
print("--- Reading File ---")
with open("buggy_code.py", "r") as file:
    bad_code = file.read()

print(f"Original Code:\n{bad_code}")

# 3. The Prompt (The Instructions)
# We tell the AI strictly what to do.
prompt = f"""
You are a Senior Python Developer. Review this code.
1. Fix all syntax and logic errors.
2. Add comments explaining the fixes.
3. Return ONLY the fixed python code. No chat, no markdown.

CODE TO FIX:
{bad_code}
"""

print("\n--- Consulting AI Tech Lead... ---")
response = model.generate_content(prompt)
fixed_code = response.text

# 4. Clean up the response (Gemini sometimes adds ```python blocks)
fixed_code = fixed_code.replace("```python", "").replace("```", "")

print("\n--- Saving Fix ---")
# 5. Write the Fixed File
with open("fixed_code.py", "w") as file:
    file.write(fixed_code)

print("Success! Check 'fixed_code.py' for the solution.")