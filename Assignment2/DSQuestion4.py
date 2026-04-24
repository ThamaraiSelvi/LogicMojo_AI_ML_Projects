## 4. Feature Engineering

#You are given:

#```python
data = [
    {"salary": 50000, "experience": 2},
    {"salary": 100000, "experience": 5}
]
#```

#Task:

#
# 1. Write a function feature_engineer(record)
def feature_engineer(record):
    record["salary_per_exp"] = record["salary"] / record["experience"] if record["experience"] > 0 else 0
    return record

# 2. Apply the function to all records
updated_data = list(map(feature_engineer, data))

# 3. Return the updated dataset
print(updated_data)
