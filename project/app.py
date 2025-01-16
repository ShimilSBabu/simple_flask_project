from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

# Load the model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from the request
    data = request.get_json()
    print(f"Data received: {data} data['features'] : {data['features']}")
    input_features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(input_features)
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
