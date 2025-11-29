# The Task
# Extract the City: Print "Report for [City Name]".
# Calculate Average Temp:
# Create a variable total_temp = 0.
# Loop through the "forecast" list.
# Add each day's temp to the total.
# Divide by the number of days (len(list)).
# Bonus (Rain Check): Count how many days have rain set to True.
weather_data = {
    "city": "Mumbai",
    "forecast": [
        {"day": "Mon", "temp": 30, "rain": False},
        {"day": "Tue", "temp": 28, "rain": True},
        {"day": "Wed", "temp": 32, "rain": False},
        {"day": "Thu", "temp": 27, "rain": True}
    ]
}

# 1. Get the list
daily_list = weather_data["forecast"]

total_temp = 0
rainy_days = 0

# 2. Loop through the list
for day_data in daily_list:
    # NOW: day_data is just one dictionary: {"day": "Mon", "temp": 30...}
    
    # Task A: Add temp to total
    # logic: total = total + current_temp
    total_temp += day_data["temp"]
    
    # Task B: Check for rain
    # logic: IF the value of "rain" is True...
    if day_data["rain"] == True:
        rainy_days += 1

# 3. Final Math
# Use len(daily_list) to get 4
avg_temp = total_temp / len(daily_list)

print(f"Average Temp: {avg_temp}")
print(f"Days with Rain: {rainy_days}")

