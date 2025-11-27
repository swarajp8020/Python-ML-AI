# Write a program that asks for your name and age, calculates the year you turn 100, and prints it using an f-string.
# name = input("Enter Name: ")
# age_string = input("How Old are you? ")
# age = int(age_string)
# current_year = 2025
# years_left = 100-age
# turn_100_year = current_year + years_left
# print(f"Hi{name}, your {age} young")
# print(f"You will turn 100 years old in the year {turn_100_year}.")
#if-else
name = input("Enter Name: ")
age_string = input("How Old are you? ")
age = int(age_string)
current_year = 2025

if age<=0:
    print("You're not born yet")
elif age>=100:
    print("You're Legend, you crossed 100 already")
else:
    years_left = 100-age
    turn_100_year = current_year + years_left
    print(f"Hi {name}, your {age} young")
    print(f"You will turn 100 years old in the year {turn_100_year}.")