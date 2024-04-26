#!/usr/bin/env python
# coding: utf-8

# In[13]:


https://github.com/patriciameka/repository/blob/branch/streamlit_app.py


# In[8]:


import requests

city = input("Location")

url = "https://yahoo-weather5.p.rapidapi.com/weather"

querystring = {"location":city,"format":"json","u":"c"}

headers = {
	"X-RapidAPI-Key": "d08767a234msh296bc12e16eddd1p12b63ajsn93ad5e1bd938",
	"X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

