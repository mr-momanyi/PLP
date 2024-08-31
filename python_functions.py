Python 3.13.0a4 (tags/v3.13.0a4:9d34f60, Feb 15 2024, 17:00:30) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def calculate_discount(price, discount_percent):
...     if discount_percent >= 20:
...         discount_amount = price * (discount_percent / 100)
...         final_price = price - discount_amount
...         return final_price
...     else:
...         return price
... 
...     
>>> original_price = float(input("Enter the original price of the item: "))
Enter the original price of the item: 450
>>> discount_percent = float(input("Enter the discount percentage: "))
Enter the discount percentage: 20
>>> 
>>> final_price = calculate_discount(original_price, discount_percent)
>>> 
>>> if discount_percent >= 20:
...     print(f"The final price after applying the discount is: {final_price}")
... else:
...     print(f"No discount applied. The original price is: {original_price}")
... 
...     
The final price after applying the discount is: 360.0
