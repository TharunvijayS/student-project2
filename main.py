import requests
import streamlit as st

apikey = "Qrxir1kPFW5KxlRRveIJYNnFpzLOaQawuhNa7EN0"
url = "https://api.nasa.gov/planetary/apod?api_key=Qrxir1kPFW5KxlRRveIJYNnFpzLOaQawuhNa7EN0"

response1=requests.get(url)
content=response1.json()

title=content["title"]
image_url=content["url"]
explanation=content["explanation"]

image_filepath="image.jpg"
response2=requests.get(image_url)
with open(image_filepath,'wb')as file:
    file.write(response2.content)

st.set_page_config(layout='centered')
st.title(title)
st.image(image_filepath)
st.write(explanation)



