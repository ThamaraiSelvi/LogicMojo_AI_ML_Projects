#Question 4:- A web platform records the hours when users log into the system.


login_hours = [1, 3, 5, 7, 2, 6, 8, 4, 9, 10]
#Write a Python program that:

#Separates login hours into even-hour logins and odd-hour logins.
even_hours = [hour for hour in login_hours if hour % 2 == 0]
odd_hours = [hour for hour in login_hours if hour % 2 != 0]

#Identifies login hours that fall into peak activity time (hours greater than 5).
peak_hours = [hour for hour in login_hours if hour > 5]

#Sorts the login hours in ascending order.
login_hours.sort()

#Calculates how many logins occurred during peak hours.
peak_login_count = len(peak_hours)