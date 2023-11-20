import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Read the data
df = pd.read_csv("PATIENTDATA.csv")

# Plotting histogram
df_show = df[df['No-show'] == 'No']
df_no_show = df[df['No-show'] == 'Yes']
st.set_option('deprecation.showPyplotGlobalUse', False)
plt.hist(df_show['Age'], alpha=0.5, color='purple', label='Showed up')
plt.hist(df_no_show['Age'], alpha=0.5, color='pink', label="Didn't show up")
plt.legend()
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Appointment Attendance by Age')
st.pyplot()

subset= st.slider("enter your desired size", min_value=1, max_value=len(df), value=10)
st.dataframe(df.head(subset))
