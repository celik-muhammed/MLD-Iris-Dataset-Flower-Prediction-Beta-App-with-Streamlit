
import streamlit as st
import pandas as pd
import numpy as np

import pickle
model = pickle.load(open("final_model_iris", "rb"))

st.title("the app prediction iris flower dataset")
# st.success('This is a success message!')
# st.info('This is a purely informational message')
# st.error('This is an error')

st.sidebar.header("User input parameter")

def user_input_data():

    sepal_length=st.sidebar.slider('sepal lengrh1',4.3,7.9,5.4)
    sepal_width=st.sidebar.slider(' sepal width',2.0,4.4,3.4)
    petal_length=st.sidebar.slider('petal length',1.0,6.0,1.3)
    petal_width=st.sidebar.slider('petal width ',0.1,2.5,0.2)
    data={'sepal_length':sepal_length,
            'sepal_width':sepal_width,
            'petal_length':petal_length,
            'petal_width':petal_width}

    features=pd.DataFrame(data,index=[0])
    return features

input_df = user_input_data()

if st.button("Predict"): 
    pred = model.predict(input_df)
    st.success(f'Prediction: {pred[0]}')
