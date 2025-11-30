weather_data = {
    "city": "Mumbai",
    "forecast": [
        {"day": "Mon", "temp": 30, "rain": False},
        {"day": "Tue", "temp": 28, "rain": True},
        {"day": "Wed", "temp": 32, "rain": False},
        {"day": "Thu", "temp": 27, "rain": True}
    ]
}
def analyzer_data(data):
    daily_data = data["forecast"]
    total=0
    rainy_days = 0
    for day_data in daily_data:
        total+=day_data["temp"]
        if day_data["rain"]==True:
            rainy_days+=1
    avg = total/len(daily_data)
    return avg,rainy_days
mumbai_avg_weather,rainy_days = analyzer_data(weather_data)
print(f"Mumbai Weather: {mumbai_avg_weather}")
print(f"Rainy Days: {rainy_days}")
        