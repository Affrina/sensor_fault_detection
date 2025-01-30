import pandas as pd
from sklearn.ensemble import IsolationForest

class SensorAnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)

    def train(self, data):
        self.model.fit(data[["Sensor Value"]])

    def predict(self, sensor_value):
        return "Anomaly" if self.model.predict([[sensor_value]])[0] == -1 else "Normal"

# Load sensor data and train model
df = pd.read_csv("data/sensor_data.csv")
detector = SensorAnomalyDetector()
detector.train(df)
