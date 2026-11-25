import streamlit as st
import pandas as pd
import numpy as np

# ----------------> My First Streamlit App

st.title("My First Streamlit Application")
st.write('Hello, Welcome to my first streamlit Application')
st.write("Streamlit allows us to build data app using only python!!")


# ---------------> Test and Markdown Display

st.title("Text display in Streamlit")
st.header('This is a Header')
st.subheader('This is a Sub-header')
st.text('This is a Plain Text')

st.markdown("""
### Markdown Support

you can write **Bold-Text**, *Italic-Text* and Create List;
- item 1
- item 2
- item 3
""")


# ------------------> User input - Text input

st.title("User input Example")
name = st.text_input("Enter your Name: ")

if name:
    st.write(f"Hello {name}, Welcome to my Streamlit App.")


# ------------------> Sliders and Numbers input

st.title("Interactive Sliders")

age = st.slider("Select Your Age",0 ,100, 25)
st.write("Your Age is: ", age)

number = st.number_input("Enter a Number: ",min_value= 0, max_value= 100)
st.write(f"You Entered: {number}")


# ----------------> Select Button & Action

st.title("Button Example ")

if st.button("Click Me"):
    st.success("You Clicked the Button!!")


# ------------------> Select Box and Dropdowns

st.title("Select Box Example")

language = st.selectbox("Choose your fav programming language",
             ["Python","JAVA","C++","JavaScript"])

st.write("You Selected: ",language)


# ------------------> Sidebar Layout

st.title("Main Page")
st.sidebar.title("Sidebar Menu")

option = st.sidebar.selectbox("Choose a Page",
                     ["Home","About","Contact"])
st.write(f"You Selected: {option} ")


# -------------------> Column Layout

st.title("Columns Layout")

col1, col2 = st.columns(2)

with col1:
    st.header("Column 1")
    st.write("This is the first Column")

with col2:
    st.header("Column 2")
    st.write("This is the second Column")


# --------------> Display Data

st.title("Display Data")

data = {
    "Name":["Faizan","Meera","Usman"],
    "City":["Lahore","Islamabad","Pakpattan"]
}

df = pd.DataFrame(data)
st.dataframe(df)


# -----------------> Charts in Streamlit

st.title("Charts Example")

data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A","B","C"]
)

st.line_chart(data)


# --------------> Upload Files

st.title("File Upload Exmple")

uploaded_file = st.file_uploader("Upload a CSV file",type=['csv','xlsx'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Preview of Uploaded Data")
    st.dataframe(df.head())


# ----------------> Containers

st.title("Containers Example")

with st.container():
    st.write("This is inside a container")
    st.write("Useful for grouping components.")

st.write("Outside the container")


# --------------> Session State (Important)

st.title("Session State Example")

if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increase counter"):
    st.session_state.counter += 1

st.write("Container Value: ", st.session_state.counter)