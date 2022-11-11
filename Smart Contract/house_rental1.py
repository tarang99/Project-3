

################################################################################
# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
from dotenv import load_dotenv
import requests
import os
import json

from pathlib import Path


# ????? may need to add back ??? w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
################################################################################


# @TODO:
# From `crypto_wallet.py import the functions generate_account, get_balance,
#  and send_transaction

#from crypto_wallet1 import get_balance

# ?????3 fx replaced by smart contracts???? generate_account, , send_transaction
################################################################################
# KryptoJobs2Go Candidate Information

load_dotenv()

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

################################################################################
# The Load_Contract Function
################################################################################


@st.cache(allow_output_mutation=True)
def load_contract():

    # Load the contract ABI
    with open(Path('./contracts/compiled/RentalsETH_abi.json')) as f:
        rent_abi = json.load(f)

    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Load the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=rent_abi
    )

    return contract

contract = load_contract()







# Database of KryptoJobs2Go candidates including their name, digital address, rating and hourly cost per Ether.
# A single Ether is currently valued at $1,500
candidate_database = {
    "15 Fitzgibbon Ave": [
        "15 Fitzgibbon Ave, Toronto, ON M1K 3Z7",
        "0xaC8eB8B2ed5C4a0fC41a84Ee4950F417f67029F0",
        "4.3",
        360000000000000000,
        "Images/1.png",
        "Images/5.png",
        "Courtyard view : Garden view : Wifi : Dedicated workspace : Free parking on premises : HDTV : Washer – In building : Dryer – In building : Portable air conditioning",
    ],
    "66 Leahann Dr": [
        "66 Leahann Dr, Toronto, ON M1P 1B9",
        "0x2422858F9C4480c2724A309D58Ffd7Ac8bF65396",
        "5.0",
        490000000000000000,
        "Images/2.png",
        "Images/6.png",
        "Garden view : Public or shared beach access : Kitchen: Wifi : Free driveway parking on premises : Private hot tub – available all year : open specific hours : Pets allowed : Security cameras on property",
    ],
    "7 Brimley Rd (Boat House)": [
        "7 Brimley Rd S #E-39, Toronto, ON M1M 3W3",
        "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45",
        "4.7",
        410000000000000000,
        "Images/3.png",
        "Images/7.png",
        "Lake view : Beach access – Beachfront : Wifi – 10 Mbps : Dedicated workspace : Portable air conditioning : Private patio or balcony",
    ],
    "637 Lake Shore Blvd": [
        "637 Lake Shore Blvd W #631, Toronto, ON M5V 3J6",
        "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45",
        "4.1",
        250000000000000000,
        "Images/4.png",
        "Images/8.png",
        "Lake View : Waterfront : Kitchen : Wifi : Free parking on premises : HDTV with Netflix : Elevator : Washer : Dryer : Security cameras on property",
    
    ],
}


houses = ["15 Fitzgibbon Ave", "66 Leahann Dr", "7 Brimley Rd (Boat House)", "637 Lake Shore Blvd"]

with st.container():
    
    def get_house():
        """Display the database of KryptoJobs2Go candidate information."""
        db_list = list(candidate_database.values())

        for number in range(len(houses)):
            image_column, text_column = st.columns(2)
            with image_column:
                st.image(db_list[number][4], width=200)
                st.image(db_list[number][5], width=200)
            with text_column:
                st.write(" - **Location:** ", db_list[number][0])
                st.write(" - **Ethereum Account Address:** ", (db_list[number][1]))
                st.write(" - **Amenties -** ", db_list[number][6])
                st.write(" - **Customer Rating:** ", db_list[number][2])
                st.write(" - **Daily Rate per WEI :** ", db_list[number][3], "wei")
                st.text(" \n")
                st.write("___")
                

# Streamlit application headings
st.markdown("# VACATION RENTAL FINDER!:house:")
st.markdown("## Find The Best Vacation Rental!")
st.text(" \n")

################################################################################
# Streamlit Sidebar Code - Start

st.sidebar.markdown("## Client Account Address and Ethernet Balance in Ether")

##########################################
# Step 1 - Part 4:
# Create a variable named `account`. Set this variable equal to a call on the
# `generate_account` function. This function will create the KryptoJobs2Go
# customer’s (in this case, your) HD wallet and Ethereum account.

# @TODO:
#  Call the `generate_account` function and save it as the variable `account`
#account = contract.functions.withdraw(contractBalance)


# Use a Streamlit component to get the address of the artwork owner from the user

st.title("Vacation property")
#st.write("Choose an account to get started")
#accounts = w3.eth.accounts
#deposit_address = st.selectbox("Select Account to make a deposit on a property", options=accounts)
st.markdown("---")






##########################################

# Write the client's Ethereum account address to the sidebar


##########################################
# Step 1 - Part 5:
# Define a new `st.sidebar.write` function that will display the balance of the
# customer’s account. Inside this function, call the `get_balance` function and
#  pass it your Ethereum `account.address`.

# @TODO
# Call `get_balance` function and pass it your account address
# Write the returned ether balance to the sidebar
#ether_balance = get_balance(w3, accounts.address) 
#st.sidebar.write(ether_balance)

##########################################

# Create a select box to chose a FinTech Hire candidate
House = st.sidebar.selectbox("Select a House", houses)

# Create a input field to record the number of hours the candidate worked
with st.container():    
    hours = st.sidebar.number_input("Number of Days/Hours")
    check_in = st.sidebar.time_input("Check In Time")

    st.sidebar.markdown("## House Name, Number of Days, and Ethereum Address")

# Identify the FinTech Hire candidate
candidate = candidate_database[House][0]

# Write the KryptoJobs2Go candidate's name to the sidebar
st.sidebar.write(candidate)

# Identify the KryptoJobs2Go candidate's hourly rate
hourly_rate = candidate_database[House][3]

# Write the inTech Finder candidate's hourly rate to the sidebar
st.sidebar.write(hourly_rate)

# Identify the KryptoJobs2Go candidate's Ethereum Address
st.write("Select ethereum account or property you wish to make a rental purchase from")
accounts = w3.eth.accounts

candidate_address = st.selectbox("Select Account", options=accounts)

st.markdown("---")

# Write the inTech Finder candidate's Ethereum Address to the sidebar
st.sidebar.write(candidate_address)

# Write the house's name to the sidebar

st.sidebar.markdown("## Total in WEI")



daily_rate = candidate_database[House][3] * hours

# @TODO
# Write the `wage` calculation to the Streamlit sidebar
st.sidebar.write(daily_rate)




if st.sidebar.button("Send Transaction"):

    # @TODO
    # Call the `send_transaction` function and pass it 3 parameters:
    
    transaction_hash= contract.functions.withdraw(int(daily_rate), 
    candidate_address).transact({'from': candidate_address, 'gas': 1000000})
    receipt = w3.eth.waitForTransactionReceipt(transaction_hash)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))
st.markdown("---")



# Markdown for the transaction hash
st.sidebar.markdown("#### Validated Transaction Hash")

transaction_hash=0
# Write the returned transaction hash to the screen
st.sidebar.write(transaction_hash)

# Celebrate your successful payment


# The function that starts the Streamlit application

get_house()

 # Contact       
with st.container():
    st.write("___")
    st.header("We are here to help!")
    st.write('##')

    # Contact Form
    contact_form = """
    <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

