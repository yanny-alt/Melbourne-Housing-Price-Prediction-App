# 🏠 House Price Prediction Web Application

## Project Overview
This project is a **web application** designed to predict house prices based on user-provided inputs such as the number of rooms, location, property type, and other important features. The machine learning model was built using **XGBoost**, a powerful and efficient algorithm, and the application is deployed using **Streamlit**, a lightweight framework for building interactive web applications.

The goal of this project is to demonstrate the practical use of machine learning in solving real-world challenges and making these solutions accessible through an intuitive user interface.

---

## Features
- **Accurate Predictions**: Uses a trained **XGBoost regression model** to predict house prices based on key features.  
- **Interactive Web Interface**: Built with **Streamlit**, the app allows users to:
  - Input various features such as the number of rooms, bathrooms, and bedrooms.
  - Provide geospatial data like latitude, longitude, and proximity to the Central Business District (CBD).
  - Specify the property type (e.g., House or Unit) and region.
- **Dynamic Results**: Predictions are displayed in real-time based on user input.  
- **Accessible Deployment**: The app is hosted on **Streamlit Cloud**, ensuring it's publicly available.

---

## 🚀 How to Run the Project

### Prerequisites
Before running the project, ensure you have the following:
- **Python** (version >= 3.8).
- Install the required libraries by running:
  ```bash
  pip install streamlit xgboost numpy pickle-mixin
