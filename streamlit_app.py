import streamlit as st

# Set the title of the app
st.title("My Streamlit App")

# Add a subtitle
st.subheader("Welcome to my first Streamlit app!")

# Add some text
st.write("This is a simple example to demonstrate Streamlit's features.")

# Create an input widget (text input)
name = st.text_input("Enter your name:")

# Create a slider widget
age = st.slider("Select your age:", 0, 100, 25)

# Display the input data
st.write(f"Hello, {name}! You are {age} years old.")

# Add a button
if st.button("Click Me"):
    st.write("Button clicked!")

# Add an image (optional, if you have an image file)
# st.image("path/to/your/image.png", caption="Sample Image")

# Add a data table (using Pandas DataFrame)
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 30, 22, 29],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)

st.write("Here's a sample data table:")
st.dataframe(df)

# Add a line chart (using Pandas DataFrame)
st.write("Here's a sample line chart:")
chart_data = pd.DataFrame(
    data={
        "First": [1, 2, 3, 4],
        "Second": [10, 20, 30, 40],
        "Third": [100, 200, 300, 400]
    }
)

st.line_chart(chart_data)
