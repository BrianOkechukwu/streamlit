#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pickle
import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image


# **Loading the model**

# In[2]:


pickle_in = open('clasif(telecom).pkl', 'rb')


# In[3]:


clasif = pickle.load(pickle_in)


# In[4]:


def welcome():
    return 'welcome all'
  
# defining the function which will make the prediction using 
# the data which the user inputs
def prediction(ed, tenure, income, employ):  
   
    prediction = clasif.predict(
        [[ed, tenure, income, employ]])
    print(prediction)
    return prediction
      
  
# this is the main function in which we define our webpage 
def main():
      # giving the webpage a title
    st.title("Telecomms Company Customer Category Prediction")
      
    # here we define some of the front end elements of the web page like 
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Predict what category a customer fall under in the company! </h1>
    </div>
    """
      
    # this line allows us to display the front end aspects we have 
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
      
    # the following lines create text boxes in which the user can enter 
    # the data required to make the prediction
    ed = st.slider("ed - 1: High School Diplomas, 2: Bachelor's Degree, 3: Master's degree, 4: PHD, 5: Professor)", 1,5,1)
    tenure = st.slider("tenure", 1,500,1)
    income = st.slider("income", 5,10000,5)
    employ = st.slider("employ", 0,100,0)
    result =""
      
    # the below line ensures that when the button called 'Predict' is clicked, 
    # the prediction function defined above is called to make the prediction 
    # and store it in the variable result
    if st.button("Predict"):
        result = prediction(ed, tenure, income, employ)
    st.success('The output is {}'.format(result))
     
if __name__=='__main__':
    main()


# In[ ]:




