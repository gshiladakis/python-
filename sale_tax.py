# Ask the user to enter the purchase amount
purchase = float(input("Enter the amount of the purchase: "))

# Tax rates
state_tax_rate = 0.04
county_tax_rate = 0.02

# Calculate taxes
state_tax = purchase * state_tax_rate
county_tax = purchase * county_tax_rate
total_sales_tax = state_tax + county_tax

# Calculate total sale
total_sale = purchase + total_sales_tax

# Display results 
print("Purchase Amount: $", purchase)
print("State Sales Tax: $", state_tax)
print("County Sales Tax: $", county_tax)
print("Total Sales Tax: $", total_sales_tax)
print("Total Sale: $", total_sale)
