import streamlit as st

def calculate(num1, num2, operation):
    if operation == "Add":
        return num1 + num2
    elif operation == "Subtract":
        return num1 - num2
    elif operation == "Multiply":
        return num1 * num2
    elif operation == "Divide":
        return num1 / num2 if num2 != 0 else "Error! Division by zero."
    else:
        return "Invalid operation"

# Streamlit application
st.title("Digital Calculator")

# Input fields
num1 = st.number_input("Enter first number:")
num2 = st.number_input("Enter second number:")

# Operation selection
operation = st.selectbox("Select operation:", ["Add", "Subtract", "Multiply", "Divide"])

# Calculate button
if st.button("Calculate"):
    result = calculate(num1, num2, operation)
    st.write(f"Result: {result}")

# Clear button
if st.button("Clear"):
    st.experimental_rerun()
