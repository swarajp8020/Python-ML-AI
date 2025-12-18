import requests
import os
import sys

def scan_and_fix(folder_path):
    print(f"--Scanning {folder_path}")
    # ... YOUR LOGIC GOES HERE ...
    # 1. List files in 'folder_path'
    # 2. Loop through them
    # 3. If buggy -> Send to API -> Save Fixed Version
    url = "http://127.0.0.1:8000/review"
    files = os.listdir(folder_path)
    print(f"Scanning Folders: {os.getcwd()}")
    for file in files:
        if file.startswith("buggy_")and file.endswith(".py"):
            print(f"\n--- Found Buggy File: {file} ---")
            # Use os.path.join for safe paths
            # This creates ".\buggy_1.py" correctly on Windows
            full_file_path = os.path.join(folder_path, file)
            try:
                    with open(full_file_path,"r")as f:
                        content_of_file = f.read()
                        my_data = { "code": content_of_file }

                        print("--- Sending Order to Kitchen ---")

                        response = requests.post(url, json=my_data)
                        # Check for success before parsing
                        if response.status_code == 200:
                            result = response.json()

                            output_name = "fixed_" + file
                            # Join path for output too
                            output_path = os.path.join(folder_path, output_name)
                        
                            with open(output_path, "w") as f:
                                f.write(result["fixed_code"])
                                    
                            print(f"--- Saved to {output_name} ---")
                        else:
                             print(f"Server Error : {response.status_code}")
            except Exception as e:
                print(f"Error: file not found {file}: {e}")

def main():
    if len(sys.argv) > 1:
        folder_to_scan = sys.argv[1]
    else:
        folder_to_scan = "."
    scan_and_fix(folder_to_scan)
# The "On" Button
if __name__ == "__main__":
    main()
