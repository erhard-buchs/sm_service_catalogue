from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np
import time
import streamlit_option_menu
from streamlit_option_menu import option_menu

import streamlit_authenticator as stauth

import yaml
from yaml.loader import SafeLoader

st.set_page_config(layout="wide")

with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

authenticator.login()

if st.session_state["authentication_status"]:
   authenticator.logout()
   st.write(f'Welcome *{st.session_state["name"]}*')
   st.title('Some content')
   st.title('st.form')
   # Full example of using the with notation
   st.header('1. Example of using `with` notation')
   st.subheader('Coffee machine')
   st.title('How to layout your Streamlit app')

   with st.expander('About this app'):
      st.write('This app shows the various ways on how you can layout your Streamlit app.')
      st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

   st.sidebar.header('Input')
   user_name = st.sidebar.text_input('What is your name?')
   user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
   user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

   with st.sidebar:
      selected = option_menu(
         menu_title = "Main Menu",
         options = ["Home","Projects","Contact"],
         icons = ["house","book","envelope"],
         menu_icon = "cast",
         default_index = 0,

      )
   
   st.header('Output')

   col1, col2, col3 = st.columns(3)

   with col1:
      if user_name != '':
         st.write(f'👋 Hello {user_name}!')
      else:
         st.write('👈  Please enter your **name**!')

   with col2:
      if user_emoji != '':
         st.write(f'{user_emoji} is your favorite **emoji**!')
      else:
         st.write('👈 Please choose an **emoji**!')

   with col3:
      if user_food != '':
         st.write(f'🍴 **{user_food}** is your favorite **food**!')
      else:
         st.write('👈 Please choose your favorite **food**!')

   tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

   with tab1:
      st.header("A cat")
      st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

   with tab2:
      st.header("A dog")
      st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

   with tab3:
      st.header("An owl")
      st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
      
   tab4, tab5 = st.tabs(["📈 Chart", "🗃 Data"])
   data = np.random.randn(10, 1)

   tab4.subheader("A tab with a chart")
   tab4.line_chart(data)

   tab5.subheader("A tab with the data")
   tab5.write(data)

   with st.form('my_form'):
      st.subheader('**Order your coffee**')

      # Input widgets
      coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
      coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
      brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
      serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
      milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
      owncup_val = st.checkbox('Bring own cup')

      # Every form must have a submit button
      submitted = st.form_submit_button('Submit')

   """
   # Welcome to Streamlit!

   Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

   If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
   forums](https://discuss.streamlit.io).

   In the meantime, below is an example of what you can do with just a few lines of code:
   """

   with st.echo(code_location='below'):
      total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
      num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

      Point = namedtuple('Point', 'x y')
      data = []

      points_per_turn = total_points / num_turns

      for curr_point_num in range(total_points):
         curr_turn, i = divmod(curr_point_num, points_per_turn)
         angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
         radius = curr_point_num / total_points
         x = radius * math.cos(angle)
         y = radius * math.sin(angle)
         data.append(Point(x, y))

      st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
         .mark_circle(color='#0068c9', opacity=0.5)
         .encode(x='x:Q', y='y:Q'))    
      
    
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')



# st.title('st.form')

# # Full example of using the with notation
# st.header('1. Example of using `with` notation')
# st.subheader('Coffee machine')

# st.title('How to layout your Streamlit app')

# with st.expander('About this app'):
#   st.write('This app shows the various ways on how you can layout your Streamlit app.')
#   st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

# st.sidebar.header('Input')
# user_name = st.sidebar.text_input('What is your name?')
# user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
# user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])


# with st.sidebar:
#   selected = option_menu(
#     menu_title = "Main Menu",
#     options = ["Home","Projects","Contact"],
#     icons = ["house","book","envelope"],
#     menu_icon = "cast",
#     default_index = 0,

#   )
  
# st.header('Output')

# col1, col2, col3 = st.columns(3)

# with col1:
#   if user_name != '':
#     st.write(f'👋 Hello {user_name}!')
#   else:
#     st.write('👈  Please enter your **name**!')

# with col2:
#   if user_emoji != '':
#     st.write(f'{user_emoji} is your favorite **emoji**!')
#   else:
#     st.write('👈 Please choose an **emoji**!')

# with col3:
#   if user_food != '':
#     st.write(f'🍴 **{user_food}** is your favorite **food**!')
#   else:
#     st.write('👈 Please choose your favorite **food**!')

# tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

# with tab1:
#    st.header("A cat")
#    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

# with tab2:
#    st.header("A dog")
#    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

# with tab3:
#    st.header("An owl")
#    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
   
   
# tab4, tab5 = st.tabs(["📈 Chart", "🗃 Data"])
# data = np.random.randn(10, 1)

# tab4.subheader("A tab with a chart")
# tab4.line_chart(data)

# tab5.subheader("A tab with the data")
# tab5.write(data)

# with st.form('my_form'):
#     st.subheader('**Order your coffee**')

#     # Input widgets
#     coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
#     coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
#     brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
#     serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
#     milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
#     owncup_val = st.checkbox('Bring own cup')

#     # Every form must have a submit button
#     submitted = st.form_submit_button('Submit')

# """
# # Welcome to Streamlit!

# Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

# If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
# forums](https://discuss.streamlit.io).

# In the meantime, below is an example of what you can do with just a few lines of code:
# """

# with st.echo(code_location='below'):
#    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
#    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

#    Point = namedtuple('Point', 'x y')
#    data = []

#    points_per_turn = total_points / num_turns

#    for curr_point_num in range(total_points):
#       curr_turn, i = divmod(curr_point_num, points_per_turn)
#       angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
#       radius = curr_point_num / total_points
#       x = radius * math.cos(angle)
#       y = radius * math.sin(angle)
#       data.append(Point(x, y))

#    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
#       .mark_circle(color='#0068c9', opacity=0.5)
#       .encode(x='x:Q', y='y:Q'))