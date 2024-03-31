# Import necessary libraries
import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder

# Initialize label encoder
encoder = LabelEncoder()

# Set page configuration
st.set_page_config(page_title='Layoff Prediction',
                   page_icon='icon.webp',
                   layout='centered',
                   initial_sidebar_state='auto')

# Set the title of the web app
st.title('Layoff Prediction Application')

# Display an image and a header in the sidebar
logo = 'icon.webp'
st.sidebar.image(logo, width=150)
st.sidebar.header('Input Data')

# Function to gather user input features from the sidebar
def user_input_features():
    joining_year = st.sidebar.slider('Joining Year', 1990, 2020, 2017)
    education = st.sidebar.selectbox('Education', ('Masters', 'Bachelors', 'PHD'))
    payment_tier = st.sidebar.slider('Payment Tier', 1, 3, 2)
    city = st.sidebar.selectbox('City', ('New Delhi', 'Pune', 'Bangalore'))
    age = st.sidebar.slider('Age', 22, 60, 30)
    gender = st.sidebar.selectbox('Gender', ('Male', 'Female'))
    ever_benched = st.sidebar.selectbox('Ever Benched', ('No', 'Yes'))
    experience_in_current_domain = st.sidebar.slider("Years in Current Field", 0, 5, 2)

    # Create a dictionary of the input features
    data = {'Education': education,
            'JoiningYear': joining_year,
            'City': city,
            'PaymentTier': payment_tier,
            'Age': age,
            'Gender': gender,
            'EverBenched': ever_benched,
            'ExperienceInCurrentDomain': experience_in_current_domain}

    # Convert the input data into a pandas DataFrame
    features = pd.DataFrame(data, index=[0])
    return features

# Get user input features
input_df = user_input_features()

# Columns that need to be encoded
columns_to_encode = ['Education', 'City', 'Gender', 'EverBenched', 'ExperienceInCurrentDomain']
for column in columns_to_encode:
    input_df[column] = encoder.fit_transform(input_df[column])

# Display the input features to the user
st.subheader("Entered Data")
st.write(input_df)

# Load the pre-trained model
model = pickle.load(open('Employee.pkl', 'rb'))

# Make prediction and prediction probability
prediction = model.predict(input_df)
prediction_proba = model.predict_proba(input_df)

# Display predictions
col1, col2 = st.columns(2)

with col1:
    st.subheader('Prediction')
    st.write(prediction)

with col2:
    st.subheader('Prediction Probability')
    st.write(prediction_proba)

# Display layoff status based on the prediction
if prediction == 0:
    st.subheader('Not likely to be laid off')
else:
    st.subheader('Likely to be laid off')
