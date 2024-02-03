import plotly
import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of days")
option = st.selectbox("Select data to view",
                      ("Temperature", "sky"))

st.subheader(f"{option} for the next {days} in {place}")


def get_data(days):
    date = ["01-01-2003", "01-02-2003", "01-03-2003"]
    temperatures = [3, 4, 5]
    temperatures = [i * days for i in temperatures]
    return date, temperatures


d, t = get_data(days)
figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})

st.plotly_chart(figure)