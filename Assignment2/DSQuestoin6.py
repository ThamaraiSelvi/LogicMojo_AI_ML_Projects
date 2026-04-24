## 6. Sequence Pattern Detection

#You are given:

#```python
data = [10, 20, 30, 25, 40, 50]
#```

#Task:

#1. Write a function detect_increasing_sequence(data)
def detect_increasing_sequence(data):
    if not data:
        return []

    longest = []
    current = [data[0]]

    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            current.append(data[i])
        else:
            if len(current) > len(longest):
                longest = current
            current = [data[i]]

    return longest if len(longest) > len(current) else current
print(detect_increasing_sequence(data))

#2. Find the longest continuous increasing sequence 
#3. Return that sequence as a list


