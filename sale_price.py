# This program gets an item's original price and 
# calculates its sale price, with a 20% discount.

# Get the items' original price.
original_price = input("Enter the item's original price: ")

# Calculate the amount of the discount.
discount = original_price * 0.2

# Calcualte the sale price. 
sale_price = original_price - discount

# Display the sale price.
print 'The sale price is', sale_price
