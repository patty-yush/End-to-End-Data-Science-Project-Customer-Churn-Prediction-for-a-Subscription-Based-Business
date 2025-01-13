from flask import Flask, request, jsonify
import pickle
import numpy as np

# Load the model
with open('churn_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Initialize the Flask app
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Customer Churn Prediction API"

@app.route('/predict', methods=['POST'])  # Make sure only POST requests are allowed here
def predict():
    # Ensure the method is POST
    if request.method == 'POST':
        # Get the JSON data from the request
        data = request.get_json()

        # Make sure the 'features' key is in the data
        if 'features' not in data:
            return jsonify({'error': "Missing 'features' in request data"}), 400
        
        # Extract features (assuming 'features' is a list of values)
        features = np.array([data['features']])
        
        # Predict using the loaded model
        prediction = model.predict(features)

        # Return the prediction result as a JSON response
        return jsonify({'Churn': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
