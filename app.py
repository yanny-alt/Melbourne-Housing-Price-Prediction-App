import streamlit as st
import pickle
import numpy as np

# Title of the Web App
st.title("🏠 House Price Prediction App")

# Display a brief description of the app
st.write("""
    This web application predicts house prices based on the features provided by the user. 
    The prediction model was trained using XGBoost, and the features include the number of rooms, 
    distance to the CBD, postcode, number of bedrooms, bathrooms, latitude, longitude, land size, 
    property type, and region.
""")

# Add a sidebar with a description
st.sidebar.title("About")
st.sidebar.info("""
    This model predicts house prices based on several input features.
    The model was trained using data from Melbourne's housing market.
    The prediction is based on the following features: 
    - Number of rooms
    - Distance to the city center (CBD)
    - Postcode
    - Number of bedrooms
    - Number of bathrooms
    - Latitude and Longitude
    - Property type (House/Unit)
    - Region (Southern Metropolitan/Northern Metropolitan)
    - Land size (in square meters)
""")

# Load the pre-trained model using pickle
with open('xgb_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Function to make predictions
def predict(features):
    prediction = model.predict([features])
    return prediction[0]

# Creating a form for user inputs
st.subheader("Enter House Details")

# Create a grid-like layout with 3 columns for inputs
col1, col2, col3 = st.columns(3)

# Get user inputs for each feature in the dataset inside the columns
with col1:
    rooms = st.number_input("Number of Rooms", min_value=1, max_value=10, step=1, help="Enter the number of rooms in the house.")
    postcode = st.number_input("Postcode", min_value=1000, max_value=9999, step=1, help="Enter the postcode of the house.")
    bedroom2 = st.number_input("Number of Bedrooms (2nd)", min_value=0, max_value=10, step=1, help="Enter the number of second bedrooms.")
    latitude = st.number_input("Latitude", min_value=-90.0, max_value=90.0, step=0.1, help="Enter the latitude of the house.")
    landsize = st.number_input("Landsize (in square meters)", min_value=0, step=1, help="Enter the land size of the property.")

with col2:
    distance = st.number_input("Distance to CBD (km)", min_value=1, max_value=100, step=1, help="Enter the distance of the house from the city center.")
    bathroom = st.number_input("Number of Bathrooms", min_value=0, max_value=10, step=1, help="Enter the number of bathrooms.")
    longitude = st.number_input("Longitude", min_value=-180.0, max_value=180.0, step=0.1, help="Enter the longitude of the house.")

with col3:
    type_t = st.selectbox("Property Type", ["Type_t", "Type_u"], help="Select whether the property is a house (Type_t) or a unit (Type_u).")
    region = st.selectbox("Region", ["Southern Metropolitan", "Northern Metropolitan"], help="Select the region of the property.")

# Convert categorical variables into numeric form
type_t_numeric = 1 if type_t == "Type_t" else 0
type_u_numeric = 1 if type_t == "Type_u" else 0
region_southern_metropolitan = 1 if region == "Southern Metropolitan" else 0
region_northern_metropolitan = 1 if region == "Northern Metropolitan" else 0

# Combine all the user inputs into a list (features)
features = [
    rooms,
    distance,
    postcode,
    bedroom2,
    bathroom,
    latitude,
    longitude,
    landsize,  # Added Landsize input here
    type_t_numeric,  # Convert categorical variable to numeric
    type_u_numeric,
    region_northern_metropolitan,
    region_southern_metropolitan
]

# Display the input values (optional step to show what the user entered)
st.write("### You have entered the following details:")
st.write(f"Rooms: {rooms}")
st.write(f"Distance: {distance} km")
st.write(f"Postcode: {postcode}")
st.write(f"Bedrooms (2nd): {bedroom2}")
st.write(f"Bathrooms: {bathroom}")
st.write(f"Latitude: {latitude}")
st.write(f"Longitude: {longitude}")
st.write(f"Landsize: {landsize} square meters")
st.write(f"Property Type: {type_t}")
st.write(f"Region: {region}")

# Create a button to trigger prediction
if st.button("Predict House Price"):
    prediction = predict(features)
    
    # Show the prediction result
    st.write(f"### The predicted house price is: ${prediction:,.2f}")
    
    # Additional message with confidence (optional)
    st.write("Note: This prediction is based on the model's training with historical data, and actual house prices may vary.")

# Footer with some information about the project
st.markdown("""
    ---
    Built with ❤️ by Favour Igwezeke
    - Model: XGBoost
    - Data Source: Melbourne Housing Data
    - Deployed using Streamlit
""")
