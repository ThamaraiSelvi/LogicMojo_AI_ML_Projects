#Question 1: A digital payment platform recorded the following transaction amounts made by a customer during a single day.

transactions = [1200, 3000, 250, 7800, 540, 3000, 9100, 250, 1500, 7800]

#Write a Python program that performs the following analysis
duplicates = [item for item in set(transactions) if transactions.count(item) > 1]
print("Duplicate transactions:", duplicates)

#Detect transactions greater than ₹5000 as these may require fraud monitoring.
fraudulent_transactions = [tx for tx in transactions if tx > 5000]
print("Potential fraudulent transactions:", fraudulent_transactions)

#Calculate the total spending for the day.
total_spending = sum(transactions)
print("Total spending for the day:", total_spending)


#Create a new list containing only unique transaction values.
unique_transactions = list(set(transactions))
print("Unique transactions:", unique_transactions)

#Sort the unique transaction list in descending order to view the largest transactions first.
unique_transactions.sort(reverse=True)
print("Unique transactions (sorted):", unique_transactions)
