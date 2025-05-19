# WalkLogix

**WalkLogix** is a Python-based application that estimates calories burned during walking or jogging sessions in community parks. 
It uses a mathematical modeling approach inspired by the DLICP (Deep Learning Integrated Community Parks) framework [1] — excluding computer vision — 
to provide an accessible, low-cost alternative to wearable fitness trackers.

---

## 🚀 Features

- Register users with **name**, **age**, and **weight**
- Automatically generates a unique **User ID (UUID)** for backend tracking
- Start new sessions using just the user’s name
- Track workouts using:
  - Number of laps
  - Park perimeter (in km)
  - Time spent (in minutes)
- Calculates:
  - Distance covered
  - Average pace (km/h)
  - Calories burned (kcal)
- Saves all data into **CSV files**
- View past session statistics:
  - View **latest session**
  - Lookup by **session ID**

---

🧮 Calorie Burn Formula
Calories burned per minute:

Calories/min = (MET × Weight_kg × 3.5) / 200

Where MET is dynamically assigned based on the average walking pace.


References:

[1] https://link.springer.com/chapter/10.1007/978-3-031-66336-9_12



