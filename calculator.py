# calculator.py

def get_met(pace_kmph):
    if pace_kmph <= 3.0:
        return 2.0
    elif pace_kmph <= 4.8:
        return 3.5
    elif pace_kmph <= 6.4:
        return 5.0
    else:
        return 6.0

def calculate_calories(weight_kg, laps, park_perimeter_km, time_min):
    distance_km = park_perimeter_km * laps
    time_hr = time_min / 60
    pace_kmph = distance_km / time_hr if time_hr > 0 else 0
    met = get_met(pace_kmph)
    cal_per_min = (met * weight_kg * 3.5) / 200
    total_calories = cal_per_min * time_min
    return {
        'distance_km': round(distance_km, 2),
        'pace_kmph': round(pace_kmph, 2),
        'calories_burned': round(total_calories, 2)
    }

