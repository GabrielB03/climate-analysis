# Climate Analysis

## Overview

Climate Analysis is a simple and user-friendly Python application for visualizing climate data such as temperature, humidity, and precipitation throughout the year. The project uses Seaborn and Matplotlib to create clear and informative visualizations that help identify seasonal patterns and trends.

## Features

- **Line Plot:** Visualize monthly temperature variation.
- **Subplots:** Display temperature, humidity, and precipitation in separate graphs.
- **Heatmap:** Show average monthly temperature by city.

## Technologies Used

- **Python:** Core programming language for data processing and visualization.
- **Pandas:** For handling and transforming CSV data.
- **Matplotlib:** For customizable plotting and layout.
- **Seaborn:** For high-level statistical visualizations.

## Project Structure

- `generate_climate_data.py`: Script that generates sample climate data and saves it to a CSV file.
- `climate_analysis.py`: Main script for loading, analyzing, and visualizing the climate data.
- `requirements.txt`: Contains the dependencies required to run the project.

## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Generate the CSV data:
   ```bash
   python generate_climate_data.py
   ```
3. Run the analysis:
   ```bash
   python clmate_analysis.py
   ```
4. To switch between light and dark themes, edit the theme variable in climate_analysis.py:
   ```bash
   theme = "dark"  # or "light"
   ```

# Project Test

![image](https://github.com/user-attachments/assets/2f98ca1b-6a02-4903-9d60-27d9353012cf)

![image](https://github.com/user-attachments/assets/4bbcaa44-3aac-45bc-bbab-811913e569d4)

![image](https://github.com/user-attachments/assets/be7a5bb0-1e19-4515-a4f1-230f1f06395c)
