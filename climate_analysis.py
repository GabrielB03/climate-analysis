import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Theme options: "light" or "dark"
theme = "dark"

# Apply theme
if theme == "dark":
    plt.style.use("dark_background")
    sns.set_theme(style="darkgrid")
else:
    plt.style.use("default")
    sns.set_theme(style="whitegrid")

# Load CSV data
data = pd.read_csv("climate_data.csv")

# Lineplot - Temperature variation through the year
plt.figure(figsize=(10, 5))
sns.lineplot(data=data, x="Month", y="Temperature", marker='o')
plt.title("Monthly Temperature Variation")
plt.xlabel("Month")
plt.ylabel("Temperature (ºC)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Subplots - Temperature, Humidity, Precipitation
fig, axs = plt.subplots(3, 1, figsize=(10, 12), sharex=True)

sns.lineplot(data=data, x="Month", y="Temperature",
             ax=axs[0], marker='o', color='red')
axs[0].set_title("Temperature")

sns.lineplot(data=data, x="Month", y="Humidity",
             ax=axs[1], marker='o', color='blue')
axs[1].set_title("Humidity")

sns.lineplot(data=data, x="Month", y="Precipitation",
             ax=axs[2], marker='o', color='green')
axs[2].set_title("Precipitation")

plt.xlabel("Month")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Heatmap - Monthly average by city (pivoted)
pivot_temp = data.pivot_table(
    values="Temperature", index="City", columns="Month")
plt.figure(figsize=(10, 5))
sns.heatmap(pivot_temp, annot=True, cmap="coolwarm", fmt=".1f")
plt.title("Average Monthly Temperature by City")
plt.tight_layout()
plt.show()