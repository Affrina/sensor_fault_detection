from flask import Flask, request, jsonify, render_template
from app.model import detector

app = Flask(__name__, template_folder="../templates")

@app.route("/")
def home():
    return render_template("dashboard.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    sensor_value = data.get("sensor_value", 25)
    result = detector.predict(sensor_value)
    return jsonify({"sensor_value": sensor_value, "status": result})

if __name__ == "__main__":
    app.run(debug=True)
