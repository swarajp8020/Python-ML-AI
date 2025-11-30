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
    
    total=0
    rainy_days=0
    for day_list in daily_list:
        total += day_list["temp"]
        if day_list["rain"]==True:
            rainy_days+=1
    avg = total/len(daily_list)
    return avg,rainy_days
mumbai_avg, rain_count = analyze_weather(weather_data)
print(f"mumbai average & rainy days: {mumbai_avg}")
print(f"rain count: {rain_count}")

