## 7. Dictionary-Based Recommendation System

#You are given:

#```python
user_purchases = {
    "user1": ["apple", "banana"],
    "user2": ["banana", "orange"],
    "user3": ["apple", "orange"]
}
#```

#Task:

#1. Write a function recommend(user)
def recommend(user):
    purchased = set(user_purchases.get(user, []))
    recommendations = set()

    for other_user, items in user_purchases.items():
        if other_user == user:
            continue
        common_items = purchased.intersection(items)
        if common_items:
            recommendations.update(items)

    # Remove items already purchased by the user
    recommendations.difference_update(purchased)

    return list(recommendations)

print(recommend("user1"))
print(recommend("user2"))
print(recommend("user3"))

#2. Recommend items based on common items between users
#3. Do not recommend items already purchased by the user
#4. Use sets and dictionary iteration
