weather_data = {
    "city": "Mumbai",
    "forecast": [
        {"day": "Mon", "temp": 30, "rain": False},
        {"day": "Tue", "temp": 28, "rain": True},
        {"day": "Wed", "temp": 32, "rain": False},
        {"day": "Thu", "temp": 27, "rain": True}
    ]
}
def analyze_weather(data):
    daily_list = data["forecast"]

    total = 0

    for day_list in daily_list:
        total += day_list["temp"]

    avg = total / len(daily_list)

    return avg
mumbai_avg = analyze_weather(weather_data)
print(f"Average of Mumbai {mumbai_avg}")