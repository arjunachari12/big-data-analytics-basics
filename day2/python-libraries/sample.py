import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(0)
dates = pd.date_range(start='2022-01-01', end='2022-12-31', freq='D')
data = pd.DataFrame({
    'Date': dates,
    'Temperature': np.random.randint(low=-10, high=30, size=len(dates)),
    'Humidity': np.random.randint(low=30, high=90, size=len(dates)),
    'Rainfall': np.random.randint(low=0, high=20, size=len(dates))
})

# Display sample data
print("Sample Data:")
print(data.head())

# Summary statistics
print("\nSummary Statistics:")
print(data.describe())

# Line plot of Temperature over time
plt.figure(figsize=(10, 5))
plt.plot(data['Date'], data['Temperature'], color='blue')
plt.title('Temperature Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()

# Scatter plot of Humidity vs. Rainfall
plt.figure(figsize=(8, 6))
plt.scatter(data['Humidity'], data['Rainfall'], color='green', alpha=0.5)
plt.title('Humidity vs. Rainfall')
plt.xlabel('Humidity (%)')
plt.ylabel('Rainfall (mm)')
plt.grid(True)
plt.show()
