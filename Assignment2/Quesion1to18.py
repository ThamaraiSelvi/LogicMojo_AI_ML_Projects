#Q1. Division with Exception Handling
#Write a program that takes two numbers and safely performs division.
#Handle division by zero using try-except.
def safe_divide(num1, num2):
    try:
        result = num1 / num2
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

# Get user input
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

safe_divide(number1, number2)

#Q2. String to Integer Conversion

#Given a list:

data = ["10", "20", "abc", "30"]

#Convert all values to integers.
#Skip invalid values using exception handling.

converted_data = []
for item in data:
    try:
        value = int(item)
        converted_data.append(value)
    except ValueError:
        continue

print("Converted Data:", converted_data)

#Q3. Multiple Exception Handling

#Write a program that:

#Takes user input
#Converts it to integer
#Divides 100 by that number

#Handle:

#ValueError
#ZeroDivisionError

def divide_by_user_input():
    user_input = input("Enter a number: ")
    try:
        num = int(user_input)
        result = 100 / num
        print("Result:", result)
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

#Q4. Using finally

#Write a program that:

#Opens a file (dummy)
#Prints a message
#Ensures a “Closing file” message always runs using finally

try:
    file = open("dummy.txt", "w")
    file.write("Hello, World!")
    print("File written successfully.")
except Exception as e:
    print("Error:", e)
finally:
    file.close()
    print("Closing file.")

#Q5. Using assert

#Write a program that checks if a number is positive using assert.

def check_positive_number(num):
    assert num > 0, "Error: Number is not positive."
    print("Number is positive.")

# Test the function
try:
    check_positive_number(5)
    check_positive_number(-3)
except AssertionError as e:
    print(e)

#Q6. Clean Text

#Given:

text = "   Hello Python   "

#Remove spaces and convert to lowercase.
cleaned_text = text.strip().lower()
print("Cleaned Text:", cleaned_text)    

#Q7. Replace Words

#Replace all occurrences of "Python" with "AI" in:

#text = "Python is great. Python is easy."

replaced_text = text.replace("Python", "AI")
print("Replaced Text:", replaced_text)

#Q8. Split and Join

#Convert:

text = "apple,banana,orange"
#Into:
#"apple banana orange"

split_text = text.split(",")
joined_text = " ".join(split_text)
print("Joined Text:", joined_text)

#Q9. Count Words

#Count number of words in a sentence using split.

text = "Hello world, this is a test."
word_list = text.split()
word_count = len(word_list)
print("Number of words:", word_count)

#Q10. Reverse Words

#Reverse words in a string:

text = "I love AI"
reversed_text = " ".join(reversed(text.split()))
print("Reversed Text:", reversed_text)

#Q11. Find Digits

#Extract all digits from:

text = "My number is 98765"
digit_list = [char for char in text if char.isdigit()]
print("Digits found:", digit_list)

#Q12. Find Words Starting with 'a'

#From:

text = "apple banana avocado berry"

#Extract words starting with 'a'.
word_list = text.split()
a_words = [word for word in word_list if word.startswith('a')]
print("Words starting with 'a':", a_words)

#13. Extract Emails

#Extract emails from:

text = "Contact: test@gmail.com, admin@yahoo.com"

email_list = [word for word in text.split() if "@" in word]
print("Emails found:", email_list)

#Q14. Validate Phone Numbers

#Extract valid 10-digit phone numbers from:

text = "Call 9876543210 or 12345"

phone_list = [word for word in text.split() if word.isdigit() and len(word) == 10]
print("Valid Phone Numbers found:", phone_list)

#Q15. Replace Digits

#Replace all digits with "X" in:

text = "My number is 98765"

replaced_text = "".join("X" if char.isdigit() else char for char in text)
print("Replaced Text:", replaced_text)

#Q16. Extract Dates

#Extract date from:

text = "Today is 2026-03-28"

#Return:

#Year: 2026
#Month: 03
#Day: 28        


#Q. 17 Extract numbers followed by "rs":

text = "100rs 200usd 300rs"

rs_numbers = [word[:-2] for word in text.split() if word.endswith("rs")]
print("Numbers followed by 'rs':", rs_numbers)

#Q. 18 Extract numbers that come after "rs":

text = "rs100 rs200 usd300"

rs_numbers = [word[2:] for word in text.split() if word.startswith("rs")]
print("Numbers that come after 'rs':", rs_numbers)
