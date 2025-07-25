# File: explore_datetime.py
# Objective: Work with Python's datetime module

from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format it
    print("Current date and time:", formatted_date)

def calculate_future_date():
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days_to_add)
        print("Future date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Please enter a valid integer.")

# Call the functions
display_current_datetime()
calculate_future_date()
