# Tip, Tax, Total Program

# Ask the user for the food charge
food_charge = float(input("Enter the change for the food: $"))

# Calcualte tip and tax
tip = food_charge * 0.15
tax = food_charge * 0.07

# Calculate total amount
total = food_charge + tip + tax

# Display results
print("\nMeal Cost: $" format(food_charge, ".2f"))
print("Tip (15%): $", format(tip, ".2f"))
print("Sales Tax (7%): $", format(tax, ".2f"))
print("Total Amount: $", format(total, ".2f"))
