import requests
from transformers import pipeline
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the NLP model
nlp_model = pipeline("text-generation", model="gpt-3.5-turbo")  # Example model

def fetch_weather_data(location):
    """Mock function to fetch weather data."""
    # In real implementation, integrate with a weather API
    return {"temperature": 23, "humidity": 78, "forecast": "clear"}

@app.route('/get_crop_advice', methods=['POST'])
def get_crop_advice():
    data = request.json
    crop_type = data['crop']
    location = data['location']
    
    # Fetch required data
    weather_data = fetch_weather_data(location)
    
    # Generate advice based on data inputs
    advice = nlp_model(f"Provide advice for {crop_type} in conditions: {weather_data}")
    return jsonify({"advice": advice[0]['generated_text']})

if __name__ == '__main__':
    app.run(debug=True)
