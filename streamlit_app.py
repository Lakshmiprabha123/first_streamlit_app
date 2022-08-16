import streamlit
import pandas
streamlit.title('My parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🍇Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale , spinach  & Rocket Smoothie')
streamlit.text('🍗🍖Hard-Boiled Free Range Egg')
streamlit.header('🍌🍓Build you own Fruit Smoothie 🥝🍇')
fruits_selected=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index)), ['Avacado','Strawberries']
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
# streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)
