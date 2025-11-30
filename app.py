import streamlit as st
import numpy as np
from model import train


st.title("Hello world AI App")
st.subheader("simple linear regression model")
model = train()

st.sidebar.title("Input Features")
input_value = st.sidebar.number_input("select a value f c",1,10,1)

input_array = np.array([[input_value]])
prediction = model.predict(input_array)

st.write(f'Prediction for input {input_value}')
st.write(f'The predicted output is: {prediction[0]:.2f}')