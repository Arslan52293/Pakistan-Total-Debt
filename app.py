import streamlit as st

# Define the page routing
PAGES = {
    "Debt Analysis (2011-2024)": "page1.py",
    "Govt to Govt Debt": "page2.py"
}

# Sidebar for navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Select a Page", list(PAGES.keys()))

# Load and display the selected page
if selection:
    page_path = PAGES[selection]
    exec(open(page_path).read())



