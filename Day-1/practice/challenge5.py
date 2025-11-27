# Task 2: The Grade Book (Dicts)
# Create a dictionary: grades = {"Math": 90, "Science": 85, "English": 78}.
# Ask the user: "Which subject score do you want?"
# If the subject exists, print the score.
# If it doesn't exist, print "Subject not found, adding it now..." and ask for the score, then add it to the dictionary.
# Print the final dictionary.

grades = {"Math": 90, "Science": 85, "English": 78}
subjects = input("Which subject score do you want? ").strip().title()
if subjects in grades:
    print(f"Subject {subjects}:{grades[subjects]}")
else:
    print(f"Subject '{subjects}' not found!")

    new_score = int(input(f"Enter Marks of {subjects}: "))
    
    grades[subjects] = new_score
    print("Added Successfully")
print("Final Report card",grades)
    