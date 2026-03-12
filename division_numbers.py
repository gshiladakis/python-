def print_div(op_1, op_2):
  """ Prints division operation """
  print(f"{op_1}/{op_2} = {op_1/op_2}")

num_1 = 6
num_2 = 3
print_div(num_1, num_2) # Prints "6/3 = 2.0"
print_div(num_2, num_1) # Prints "3/6 = 0.5"
print_div(num_1) # Error: Missing argument: op_2
