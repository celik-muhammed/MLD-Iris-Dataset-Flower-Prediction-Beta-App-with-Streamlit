
import streamlit as st
import pandas as pd
import numpy as np
import pickle

model = pickle.load(open("final_model_iris", "rb"))

st.markdown("<h2 style='text-align:center; color:floralWhite;'>Iris Dataset Flower Prediction Beta App</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,8,1]) 
#Image
try:
    #image url
    url = "https://editor.analyticsvidhya.com/uploads/51518iris%20img1.png"
    
    with col2:
        st.image(url, caption="Predicting the Prices of Cars")
    
except:
    # Executed if error in the 
    st.text("Image Not Loading!")
    components.html('''
    <script>
        alert("Image Not Loading!");
    </script>
    ''')        


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

st.sidebar.header("User input parameter")
input_df = user_input_data()

if st.button("Predict"): 
    pred = model.predict(input_df)
    st.success(f'Prediction: {pred[0]}')
