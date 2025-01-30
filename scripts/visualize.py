import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/sensor_data.csv")

def plot_sensor_data():
    plt.figure(figsize=(10, 5))
    plt.plot(df["Timestamp"], df["Sensor Value"], label="Sensor Data", color="blue")
    plt.xlabel("Timestamp")
    plt.ylabel("Sensor Value")
    plt.title("Sensor Data with Anomaly Detection")
    plt.legend()
    plt.xticks(rotation=45)
    plt.show()

if __name__ == "__main__":
    plot_sensor_data()
