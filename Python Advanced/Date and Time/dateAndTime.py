from datetime import datetime

# current time
now = datetime.now()
print("Current date and time:", now)

# Manipulating Dates and Times
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)

# formatting Dates and Times
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date and time:", formatted_date)

# Creating Specific Dates and Times:
event_date = datetime(2023, 12, 25, 10, 30, 45)
print("Event date and time:", event_date)

difference = now - event_date
print("Days until event:", difference.days)
