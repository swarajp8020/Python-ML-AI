import google.generativeai as genai
import config

# Configure the key
genai.configure(api_key=config.GEMINI_API_KEY)

print("--- 📋 Google's Menu for You ---")
try:
    for m in genai.list_models():
        # We only want models that can 'generateContent' (Chat)
        if 'generateContent' in m.supported_generation_methods:
            # removing 'models/' prefix to make it easy to read
            clean_name = m.name.replace("models/", "")
            print(f"- {clean_name}")
except Exception as e:
    print(f"❌ Error connecting to Google: {e}")