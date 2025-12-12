# Import the library
import google.generativeai as genai
from config import GEMINI_API_KEY

# 1. SETUP THE AI
# (Use genai.configure and set the model to 'gemini-flash-latest')
# ... WRITE CODE HERE ...
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-flash-latest')


# 2. READ THE FILE
# (Open "buggy_code.py" in 'r' (read) mode. Save content to a variable called 'code_content')
print("--- Reading File ---")
# ... WRITE CODE HERE ... (Hint: use 'with open...')
with open("buggy_code.py","r") as f:code_content = f.read()

# 3. CREATE THE PROMPT
# (Create a string variable. Tell the AI: "Fix this code: " + code_content)
prompt = f"Fix this python code and return ONLY code:\n{code_content}"


# 4. SEND TO AI
# (Pass the prompt to the model. Save the result in 'response')
print("--- Sending to AI ---")
# ... WRITE CODE HERE ...
response = model.generate_content(prompt)

# 5. WRITE THE FILE
# (Open "fixed_code_v2.py" in 'w' (write) mode. Write response.text inside it)
print("--- Saving Fix ---")
# ... WRITE CODE HERE ...
with open("new file","w")as f:f.write(response.text)

print("Done.")