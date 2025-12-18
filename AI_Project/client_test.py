import requests # The tool to visit websites via code
import os

def scan_and_fix(folder_path):
    print(f"--Scanning {folder_path}")
    

if __name__ == "__main__":
     scan_and_fix(".")

url = "http://127.0.0.1:8000/review"
files = os.listdir(".")
print(f"Scanning Folders: {os.getcwd()}")
for file in files:
    if file.startswith("buggy_")and file.endswith(".py"):
        print(f"\n--- Found Buggy File: {file} ---")
        try:
                with open(file,"r")as f:
                    content_of_file = f.read()
                    my_data = { "code": content_of_file }

                    print("--- Sending Order to Kitchen ---")

                    response = requests.post(url, json=my_data)

                    result = response.json()
                        # Save the result to a new file
                    output_name = "fixed_" + file
                    with open(output_name, "w") as f:
                        f.write(result["fixed_code"])
                            
                    print(f"--- Saved to {output_name} ---")
        except Exception as e:
            print(f"Error: file not found {file}: {e}")

