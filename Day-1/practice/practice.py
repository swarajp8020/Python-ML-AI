name = input("Your Name: ")
age = int(input("Your Age: "))
current_year = 2025
if age<=0:
    print("U! Not born yet!")
elif age>=100:
    print("Legend! U crossed 100")
else:
    years_left = 100 -age
    age_100_years = current_year+years_left
    print(f"Hi {name}, you're {age}")
    print(f"You will turn 100 in {age_100_years}")
