import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 1. Setup Time Array (5 hours of data at 1Hz)
seconds = 18000
t = np.arange(0, seconds, 1) 

# Create actual timestamps
start_time = datetime.now().replace(microsecond=0)
timestamps = [start_time + timedelta(seconds=int(i)) for i in t]

df = pd.DataFrame({'Timestamp': timestamps})

# 2. Simulate "Fast Physics" (Current Jump at t=9000)
current = np.where(t < 9000, 100, 150)
df['Current_A'] = current + np.random.normal(0, 0.2, len(t))

# 3. Simulate "Slow Physics" (Voltage with Thermal Lag)
r_initial = 0.5 
# Thermal resistance drop (0.1 Ohm) with 10-min time constant
r_thermal_drop = 0.1 * (1 - np.exp(-(t - 9000)/600)) 
r_thermal_drop = np.where(t < 9000, 0, r_thermal_drop)
r_aging = 0.000001 * t 

# V = V_open_circuit + I*R
df['Voltage_V'] = 1.1 + (df['Current_A'] * (r_initial - r_thermal_drop + r_aging))
# Add small measurement noise
df['Voltage_V'] += np.random.normal(0, 0.001, len(t))

# 4. CALCULATE THE DIGITAL SOLUTION (10-Minute Window)
# Window = 600 seconds because sampling is 1Hz
window_size = 600 
df['Rolling_Median_V'] = df['Voltage_V'].rolling(window=window_size).median()

# Calculate Residue (The Delta)
df['Residue_V'] = df['Voltage_V'] - df['Rolling_Median_V']

# 5. Save for Grafana
df.to_csv('C:\\Users\\SHAMSHUDDIN MUJAHID\\Downloads\\characterization_200\\soec_10min_analysis.csv', index=False)

print("File 'soec_10min_analysis.csv' created successfully.")
print(df[['Timestamp', 'Voltage_V', 'Rolling_Median_V', 'Residue_V']].iloc[9000:9010])