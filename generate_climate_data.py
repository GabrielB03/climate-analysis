import pandas as pd

# Climate data
data = {
    "Month": [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ],
    "City": ["New York"] * 12,
    "Temperature": [2, 3, 7, 13, 18, 24, 27, 26, 21, 15, 9, 4],
    "Humidity": [65, 60, 55, 50, 55, 60, 65, 68, 70, 65, 60, 66],
    "Precipitation": [78, 70, 85, 90, 95, 100, 120, 110, 95, 80, 75, 85]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("climate_data.csv", index=False)

print("climate_data.csv generated successfully!")
