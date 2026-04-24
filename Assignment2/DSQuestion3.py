## 3. Fraud Detection Rule Engine

#You are given:

#```python
transactions = [
    {"id": 101, "amount": 5000, "location": "India"},
    {"id": 102, "amount": 200000, "location": "Unknown"},
    {"id": 103, "amount": 1000, "location": "India"}
]
#```

#Task:

#1. Write a function is_fraud(transaction)
def is_fraud(transaction):
    if transaction["amount"] > 100000 or transaction["location"] == "Unknown":
        return "fraud"
    else:
        return "safe"

#2. If amount is greater than 100000 or location is "Unknown" mark as fraud     

#3. Otherwise mark as safe 
#4. Use lambda with filter or map
#5. Return only fraud transactions
fraud_transactions = list(filter(lambda x: is_fraud(x) == "fraud", transactions))

