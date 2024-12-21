import streamlit as st  # Importing the Streamlit library for creating web applications
import json  # Importing the JSON library for handling JSON data
import hashlib  # Importing the hashlib library for hashing (not used in this code)
import os  # Importing the OS library for interacting with the operating system

# Function to hash the password
def hash_password(password, salt="kajhsdqqi"):
    # Combine the password and salt
    combined = password + salt

    # Initialize a "hash" value
    hash_value = 10

    # Process each character in the combined string
    for i, char in enumerate(combined):
        # Shift the ASCII value of the characters
        shifted = ord(char) << (i % 8)

        # XOR with the current hash value
        hash_value ^= shifted

        # Add some non-linear mixing
        hash_value = (hash_value * 67 + 7) % (2**56)

    # Convert the final hash value to a hexadecimal string
    return hex(hash_value)[2:]

# Function to check credentials
def check_credentials(email, password):
    # Check if the users.json file exists
    if os.path.exists('users.json'): 
        with open('users.json', 'r') as f:  # Open the users.json file for reading
            users = json.load(f)  # Load the JSON data from the file
        # Check if the email exists in the credentials
        if email in users["Credentials"]:
            hashed_password = hash_password(password)  # Hash the provided password
            stored_hashed_password = users["Credentials"][email]["Password"]  # Get the stored hashed password
            print(stored_hashed_password)  # Print the stored hashed password for debugging
            print(hashed_password)  # Print the hashed password for debugging
            return hashed_password == stored_hashed_password  # Compare the hashed passwords
    else:
        st.error("File users.json tidak ditemukan.")  # Show an error if the file is not found
        return False  # Return False if the file does not exist

# User interface
st.title("Login Page")  # Set the title of the page
st.markdown("<h1 style='text-align: center; color: gray;'>Welcome to Login Page</h1>", unsafe_allow_html=True)  # Display a welcome message

# Login form
email = st.text_input("email")  # Input field for the user's email
password = st.text_input("Password", type='password')  # Input field for the user's password, masked
submit_button1 = st.button("Login")  # Button for submitting the login form
submit_button2 = st.button("Sign Up")  # Button for navigating to the sign-up page

if submit_button1:  # Check if the "Login" button is clicked
    if check_credentials(email, password):  # Check the provided credentials
        st.success("Login berhasil!")  # Show a success message if login is successful
    else:
        st.error("email atau password tidak valid.")  # Show an error message if login fails

if submit_button2:  # Check if the "Sign Up" button is clicked
    st.switch_page("pages/signup.py")  # Switch to the sign-up page