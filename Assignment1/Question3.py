#Question 3:- An analyst wants to compare the price of products listed on two e-commerce platforms.

#The following data is provided:python
products = ["Laptop","Phone","Tablet","Monitor","Headphones"]  
amazon_prices = [75000, 45000, 30000, 20000, 5000]  
flipkart_prices = [72000, 47000, 31000, 19500, 4800]
#Write a Python program that:


#Combines the product names and their prices into a single data structure representing a table.
product_table = []
for i in range(len(products)):
    product_table.append({
        "Product": products[i],
        "Amazon Price": amazon_prices[i],
        "Flipkart Price": flipkart_prices[i]
    })

#Compares the price of each product across both platforms.
for product in product_table:
    if product["Amazon Price"] < product["Flipkart Price"]:
        product["Cheaper Platform"] = "Amazon"
        product["Price Difference"] = product["Flipkart Price"] - product["Amazon Price"]
    else:
        product["Cheaper Platform"] = "Flipkart"
        product["Price Difference"] = product["Amazon Price"] - product["Flipkart Price"]

#Determines which platform offers the lower price.
cheaper_products = [product for product in product_table if product["Cheaper Platform"] == "Amazon"]
if cheaper_products:
    print("Products cheaper on Amazon:")
    for product in cheaper_products:
        print(f" - {product['Product']}: {product['Price Difference']}")

#Calculates the difference between the two prices.
for product in product_table:
    if product["Cheaper Platform"] == "Amazon":
        product["Price Difference"] = product["Flipkart Price"] - product["Amazon Price"]
    else:
        product["Price Difference"] = product["Amazon Price"] - product["Flipkart Price"]

#Displays the product name, cheaper platform, and price difference.
for product in product_table:
    print(f"Product: {product['Product']}")
    print(f" - Cheaper Platform: {product['Cheaper Platform']}")
    print(f" - Price Difference: {product['Price Difference']}")