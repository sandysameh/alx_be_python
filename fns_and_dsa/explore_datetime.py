from datetime import datetime
from datetime import timedelta

def display_current_datetime():
    current_date=datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")
    return current_date

def calculate_future_date():
    days = input("Enter the number of days to add to the current date:")
    if days.isdigit(): 
        days = int(days)
        delta = display_current_datetime() +timedelta(days=days)
        
        print(f"Future date:{delta.strftime('%Y-%m-%d')}")
        return delta.strftime('%Y-%m-%d')

        
    else :
        print("Please enter a valid number")
calculate_future_date()