#A dataset exported from a database contains the following customer age values.

#python
ages = [25, 42, -1, 34, None, 52, 17, -5, 29, None, 46]
#Some entries are invalid because they are either negative numbers or missing values (None).

#Write a Python program that:
#Iterates through the dataset and removes all invalid age values.
valid_ages = []
for age in ages:
    if age is not None and age >= 0:
        valid_ages.append(age)
print("Valid ages:", valid_ages)

#Calculates the average age of valid customers.
if valid_ages:
    average_age = sum(valid_ages) / len(valid_ages)
print("Average age of valid customers:", average_age)

#Displays the list of customers whose age is greater than 30.
print("Customers older than 30:", [age for age in valid_ages if age > 30])

#Prints how many invalid entries were removed during the cleaning process.
print("Invalid entries removed:", len(ages) - len(valid_ages))