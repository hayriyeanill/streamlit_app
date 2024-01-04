import streamlit as st
import pandas as pd
import plotly.express as px

password_guess = st.text_input('What is the Password?')
if password_guess != 'streamlit_password':
  st.stop()

st.title("Palmer's Penguins")
st.markdown("Use this Streamlit app to make your own scatterplot about penguins!")
selected_species = st.selectbox("What species would you like to visualize?",
                                ["Adelie", "Gentoo", "Chinstrap"])
selected_x_var = st.selectbox('What do you want the x variable to be?',
     ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])
selected_y_var = st.selectbox('What about the y?',
     ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])

#import our dataset
penguins_df = pd.read_csv('penguins.csv')
penguins_df = penguins_df[penguins_df['species'] == selected_species]

fig = px.scatter(penguins_df,
                 x=selected_x_var,
                 y=selected_y_var
                 )

fig = px.scatter(penguins_df,
                 x=selected_x_var,
                 y=selected_y_var
                 )
fig.update_layout({'title': f'Scatterplot of {selected_species} Penguins'} )
st.plotly_chart(fig)
