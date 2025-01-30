# **Sensor Fault Detection Dashboard**

This project is a **real-time sensor fault detection dashboard** built with **Flask** and **Chart.js**. It simulates sensor data and displays it dynamically on a web-based dashboard, updating in real-time using **WebSockets**.

The dashboard visualizes simulated sensor data, and any anomaly or sensor fault is highlighted in **red**.

## **Features**

- Real-time sensor data visualization using **Chart.js**.
- **WebSocket**-based communication for live data updates.
- **Simulated sensor values** that mimic real-time sensor data.
- **Anomaly detection**: Simulated data is processed and checked for faults.
- **Flask backend**: Flask serves as the backend to simulate data and detect anomalies.
- **Responsive UI**: The dashboard adapts to different screen sizes.
- **Historical data storage**: The simulated sensor data is stored for future analysis (optional, using SQLite or PostgreSQL).

## **Tech Stack**

- **Backend**: Python, Flask, flask-socketio
- **Frontend**: HTML, CSS, JavaScript, Chart.js
- **Database**: SQLite or PostgreSQL (optional for storing historical data)
- **Deployment**: Heroku, DigitalOcean, or similar platforms

## **Installation**

To run this project locally, follow the steps below:

### **1. Clone the Repository**

```bash
git clone https://github.com/your-username/sensor_fault_detection.git
cd sensor_fault_detection
