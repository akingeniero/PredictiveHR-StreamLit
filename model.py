# Import necessary libraries
import os

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder

# Initialize the label encoder
encoder = LabelEncoder()

# Load the dataset
employee_df = pd.read_csv('Employee.csv')

# Columns that require label encoding
columns_to_encode = ['Education', 'City', 'Gender', 'EverBenched', 'ExperienceInCurrentDomain']

# Encode categorical columns
for column in columns_to_encode:
    employee_df[column] = encoder.fit_transform(employee_df[column])

# Prepare the features (X) and target (y)
X = employee_df.drop('LeaveOrNot', axis=1)  # Features
y = employee_df['LeaveOrNot']  # Target variable

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the logistic regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Make predictions on the test set
predictions = model.predict(X_test)

# Evaluate the model's accuracy
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy}")

# Save the trained model to a file
pickle.dump(model, open('Employee.pkl', 'wb'))
