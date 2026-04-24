## 8. Recursive Decision Tree Simulation

#Task:

#1. Write a recursive function decision_tree(score)
#2. If score is greater than 80 return "Approved"
#3. If score is between 50 and 80 call the function again with score plus 10
#4. If score is less than 50 return "Rejected"

def decision_tree(score):
    if score > 80:
        return "Approved"
    elif 50 <= score <= 80:
        return decision_tree(score + 10)
    else:
        return "Rejected"