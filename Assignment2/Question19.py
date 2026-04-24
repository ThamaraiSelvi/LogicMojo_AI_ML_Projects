import re

#Q. 19 Extract Valid Transaction Records Using a Single Regex Pattern

#ou are given a messy log string:

#log = """
#ID:TXN12345 | User: Mahipal_01 | Email: mahi123@gmail.com | Phone: +91-9876543210 | Amount: Rs.5000
#ID:TXN12 | User: @InvalidUser | Email: wronggmail.com | Phone: 98765 | Amount: Rs.-200
#ID:TXN99999 | User: Ravi_kumar | Email: ravi.kumar@yahoo.com | Phone: +91-9123456789 | Amount: USD300
#ID:TXN54321 | User: Sita99 | Email: sita99@gmail | Phone: +91-9999999999 | Amount: Rs.7000


#Write a single REGEX pattern that extracts ONLY VALID records where:
#CONDITIONS (VERY IMPORTANT)
#Transaction ID
#Format: TXN followed by exactly 5 digits
#Example: TXN12345
#Use: ^, {}, \d

#Username
#Only letters, numbers, underscore
#Must start with a letter
#Example: Mahipal_01
#Use: [a-zA-Z], \w, +

#Email
#Valid format: word@word.domain
#Example: test123@gmail.com
#Use: \w, ., @, +, \.

#Phone Number
#Format: +91-XXXXXXXXXX
#Exactly 10 digits
#Use: \+, \d, {}

#Amount
#Currency: Rs or USD
#Amount must be positive
#Example: Rs.5000, USD300
#Use: (rs|usd), \d+, ?


#EXPECTED OUTPUT

#Only valid records should match:

#[
#"ID:TXN12345 | User: Mahipal_01 | Email: mahi123@gmail.com | Phone: +91-9876543210 | Amount: Rs.5000",

#"ID:TXN99999 | User: Ravi_kumar | Email: ravi.kumar@yahoo.com | Phone: +91-9123456789 | Amount: USD300"
log = """
ID:TXN12345 | User: Mahipal_01 | Email: mahi123@gmail.com | Phone: +91-9876543210 | Amount: Rs.5000
ID:TXN12 | User: @InvalidUser | Email: wronggmail.com | Phone: 98765 | Amount: Rs.-200
ID:TXN99999 | User: Ravi_kumar | Email: ravi.kumar@yahoo.com | Phone: +91-9123456789 | Amount: USD300
ID:TXN54321 | User: Sita99 | Email: sita99@gmail | Phone: +91-9999999999 | Amount: Rs.7000
"""

pattern = re.compile(
    r"^ID:TXN\d{5}\s*\|\s*User:\s*[A-Za-z][A-Za-z0-9_]*\s*\|\s*"
    r"Email:\s*[A-Za-z0-9_.]+@[A-Za-z0-9_.]+\.[A-Za-z]{2,}\s*\|\s*"
    r"Phone:\s*\+91-\d{10}\s*\|\s*"
    r"Amount:\s*(?:Rs\.|USD)\d+\s*$",
    re.MULTILINE
)

valid_records = pattern.findall(log)
print(valid_records)
