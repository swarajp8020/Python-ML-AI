weather_data = {
    "city": "Mumbai",
    "forecast": [
        {"day": "Mon", "temp": 30, "rain": False},
        {"day": "Tue", "temp": 28, "rain": True},
        {"day": "Wed", "temp": 32, "rain": False},
        {"day": "Thu", "temp": 27, "rain": True}
    ]
}
daily_list=weather_data["forecast"]
total_temp = 0
rainy_days = 0
for day_list in daily_list:
    total_temp += day_list["temp"]
    if day_list["rain"]==True:
        rainy_days+=1
avg_days = total_temp/len(daily_list)
print(f"avg days {avg_days}")
print(f"rainy days {rainy_days}")