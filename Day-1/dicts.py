# Key-Value Pairs
# Notice: You can mix types! (String keys, Int values)

# Key-Value Pairs
# Notice: You can mix types! (String keys, Int values)
student = {
    "name": "Swaraj",
    "age": 25,
    "skills": ["Java", "Python"], # A List INSIDE a Dict
    "city": "Mumbai"
}

# Access
print(student["name"]) 

# Adding/Updating
student["role"] = "AI Engineer" # New key
student["age"] = 26 # Update existing

# The "Safe" Get
# If you try student["salary"], it crashes.
# Use .get() instead. It returns None if key is missing.
print(student.get("salary")) 

# Loop through keys and values
for key, value in student.items():
    print(f"{key}: {value}")