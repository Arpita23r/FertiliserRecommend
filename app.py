from flask import Flask, request, jsonify
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

data = pd.read_csv('f2.csv')
data.rename(columns={'Humidity ': 'Humidity', 'Soil Type': 'Soil_Type', 'Crop Type': 'Crop_Type', 'Fertilizer Name': 'Fertilizer'}, inplace=True)

encode_soil = LabelEncoder()
data['Soil_Type'] = encode_soil.fit_transform(data['Soil_Type'])

encode_crop = LabelEncoder()
data['Crop_Type'] = encode_crop.fit_transform(data['Crop_Type'])

encode_ferti = LabelEncoder()
data['Fertilizer'] = encode_ferti.fit_transform(data['Fertilizer'])

x_train, x_test, y_train, y_test = train_test_split(data.drop('Fertilizer', axis=1), data['Fertilizer'], test_size=0.2, random_state=1)

RF = RandomForestClassifier(n_estimators=20, random_state=0)
RF.fit(x_train, y_train)

@app.route('/suggest-fertilizer', methods=['POST'])
def suggest_fertilizer():
    data = request.get_json()
    temp = data['Temparature']
    humidity = data['Humidity']
    moisture = data['Moisture']
    soil_type = data['Soil_Type']
    crop_type = data['Crop_Type']
    nitrogen = data['Nitrogen']
    potassium = data['Potassium']
    phosphorous = data['Phosphorous']
    
    input_data = [[temp, humidity, moisture, soil_type, crop_type, nitrogen, potassium, phosphorous]]
    prediction = RF.predict(input_data)
    fertilizer_name = encode_ferti.inverse_transform(prediction)[0]
    
    return jsonify({'Fertilizer': fertilizer_name})

if __name__ == '__main__':
    app.run(debug=True)
