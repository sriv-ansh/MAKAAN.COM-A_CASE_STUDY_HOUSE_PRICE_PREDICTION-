from flask import Flask, render_template, request
import pickle
import json
import pandas as pd
from joblib import load

app = Flask(__name__)

# Load the scaling and model files
with open('Feature Scaling File/MinMax_Scaler.pkl', 'rb') as f:
    mms = pickle.load(f)

with open('Feature Scaling File/One_Hot.pkl', 'rb') as f:
    ohe = pickle.load(f)

with open('Feature Scaling File/location_dict.json', 'r') as f:
    location_dict = json.load(f)

with open("Model_File/Model.pkl", "rb") as f:
    model = pickle.load(f)

# Define the columns for one-hot encoding
one_hot_columns = ['house_type_1 Bhk Apartment', 'house_type_1 Bhk Independent Floor',
       'house_type_1 Bhk Independent House',
       'house_type_1 Rk Studio Apartment', 'house_type_2 Bhk Apartment',
       'house_type_2 Bhk Independent Floor',
       'house_type_2 Bhk Independent House', 'house_type_3 Bhk Apartment',
       'house_type_3 Bhk Independent House', 'house_type_3 Bhk Villa',
       'house_type_4 Bhk Apartment', 'house_type_4 Bhk Independent Floor',
       'house_type_4 Bhk Independent House', 'house_type_4 Bhk Villa',
       'house_type_5 Bhk Independent Floor',
       'house_type_5 Bhk Independent House', 'house_type_5 Bhk Villa',
       'city_Delhi', 'city_Mumbai', 'city_Pune', 'Status_Furnished',
       'Status_Semi-Furnished', 'Status_Unfurnished']

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    house_type = request.form.get('houseType')
    house_size = float(request.form.get('houseSize'))
    city = request.form.get('city')
    status = request.form.get('status')
    location = request.form.get('location')

    # Creating a DataFrame of the input data
    input_data = pd.DataFrame({
        'house_type': [house_type],
        'house_size': [house_size],
        'city': [city],
        'Status': [status],
        'location_map': [location_dict.get(location, 1)]
    })

    # Select and encode categorical features
    temp_df = input_data[['house_type', 'city', 'Status']]

    # One-Hot Encoding
    encoded_category_df = pd.DataFrame(ohe.transform(temp_df).toarray(),
        columns=one_hot_columns,  # Use predefined column names
        index=temp_df.index
    )

    input_data = input_data.drop(['house_type', 'city', 'Status'], axis=1).join(encoded_category_df)

    # Applying Min-Max Scaling
    input_data[['house_size', 'location_map']] = mms.transform(input_data[['house_size', 'location_map']])

    # Predict
    prediction = model.predict(input_data)
    
    print(f"Prediction: {prediction[0]}")
    return render_template('result.html', prediction= round(prediction[0],2))

if __name__ == "__main__":
    app.run(port=5001)
