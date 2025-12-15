# import requests # The tool to visit websites via code

# url = "http://127.0.0.1:8000/review"

# filename = input("Enter file to fix: ")
# try:
#     with open(filename,"r")as f:
#         content_of_file = f.read()
#         my_data = { "code": content_of_file }

#     print("--- Sending Order to Kitchen ---")

#     response = requests.post(url, json=my_data)

#     result = response.json()
#     # Save the result to a new file
#     output_name = "fixed_" + filename
#     with open(output_name, "w") as f:
#         f.write(result["fixed_code"])
        
#     print(f"--- Saved to {output_name} ---")
#     print("--- Chef's Answer ---")
#     print(result["fixed_code"])
# except FileNotFoundError:
#     print("Error: file not found")

import requests 

url = "http://127.0.0.1:8000/review"

filename = input("Enter a file to fix: ")
try:
    with open(filename, "r") as f:
        content_of_file = f.read()
        my_data = {"code":content_of_file}
    response = requests.post(url, json=my_data)
    result = response.json()
    print("--saved--")
    output_name = "fixed_"+filename
    with open(output_name, "w")as f:
        f.write = (result["fixed_code"])
    print(f"output is {output_name}")
    print("answer")
    print(result["fixed_code"])
except FileNotFoundError:
    print("Error! File not found!")