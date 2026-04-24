## 2. Text Cleaning Pipeline

#You are given:

#```python
import re


texts = [
    "Hello!!! How are you???",
    "This is    AI     class.",
    "Python@@@is###great"
]
#```

#Task:

#1. Write a function clean_text(text):
def clean_text(text):
    # 2. Remove special characters
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    # 3. Remove extra spaces
    text = re.sub(r"\s+", " ", text)
    # 4. Convert text to lowercase
    text = text.lower()
    return text

#5. Apply the function to all elements using loop or map
cleaned_texts = list(map(clean_text, texts))

#6. Return cleaned list 
print(cleaned_texts)