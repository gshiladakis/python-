# This program displays a set of salesperson
# names and units sold in two columns.

# Assign the names to variables.
salesperson1 = 'Graves'
salesperson2 = 'Harrison'
salesperson3 = 'Hoyle'
salesperson4 = 'Kramer'
salesperson5 = 'Smith'

# Assign the units sold to variables.
units1 = 1456.78
units2 = 2890.55
units3 = 946.77
units4 = 2678.91
units5 = 1287.87

# Display the data.
print('%15s %15s' % ('Salesperson', 'Units Sold'))
print('%15s %15d' % (salesperson1, units1))
print('%15s %15d' % (salesperson2, units2))
print('%15s %15d' % (salesperson3, units3))
print('%15s %15d' % (salesperson4, units4))
print('%15s %15d' % (salesperson5, units5))
