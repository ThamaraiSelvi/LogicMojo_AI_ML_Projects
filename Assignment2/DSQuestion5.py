from functools import reduce

## 5. Custom Reduce Function

#You are given:

accuracies = [0.8, 0.75, 0.9, 0.85]

#Task:

#1. Use reduce function to calculate average accuracy  
accuracies = [0.8, 0.75, 0.9, 0.85]

# 2. Do not use sum function
# 3. Show intermediate logic using a custom function

def reducer(acc, x):
    total, count = acc
    new_total = total + x
    new_count = count + 1
    print(f"Adding {x}: total {total} -> {new_total}, count {count} -> {new_count}")
    return (new_total, new_count)

total, count = reduce(reducer, accuracies, (0.0, 0))
average = total / count if count else 0.0
print("Average accuracy:", average)
#3. Show intermediate logic using a custom function     
