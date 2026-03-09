def sum_numbers(n):
  # Base case
  if n == 1:
      return 1
  else:
      return n + sum_numbers(n - 1)

# Demonstration program
number = int(input("Enter a positive integer: "))

result = sum_numbers(number)

print("The sum of numbers from 1 to", number, "is:", result)
