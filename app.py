from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

model = pickle.load(open('classifier.pkl', 'rb'))
ferti_encoder = pickle.load(open('fertilizer.pkl', 'rb'))

@app.route('/suggest-fertilizer', methods=['POST'])
def suggest_fertilizer():
    data = request.get_json()
    
    input_features = [
        data['Temparature'],
        data['Humidity'],
        data['Moisture'],
        data['Soil_Type'],
        data['Crop_Type'],
        data['Nitrogen'],
        data['Potassium'],
        data['Phosphorous']
    ]
    
    prediction = model.predict([input_features])[0]
    fertilizer_name = ferti_encoder.classes_[prediction]
    
    return jsonify({"Fertilizer": fertilizer_name})

if __name__ == '__main__':
    app.run(debug=True)
