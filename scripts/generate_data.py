import pandas as pd
import random
import numpy as np

def generate_sensor_data(num_samples=100):
    """Generates simulated sensor data with anomalies."""
    normal_data = [random.uniform(20, 30) for _ in range(num_samples - 10)]
    anomaly_data = [random.uniform(5, 15) for _ in range(5)] + [random.uniform(35, 50) for _ in range(5)]
    
    data = normal_data + anomaly_data
    timestamps = pd.date_range(start="2025-01-01", periods=num_samples, freq="T")
    np.random.shuffle(data)

    df = pd.DataFrame({"Timestamp": timestamps, "Sensor Value": data})
    df.to_csv("data/sensor_data.csv", index=False)
    print("Sensor data saved to 'data/sensor_data.csv'")

if __name__ == "__main__":
    generate_sensor_data()
