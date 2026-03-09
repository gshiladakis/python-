def sum_integers(n):
  if n == 1:          # base case
      return 1 
  else:
      return n + sum_numbers(n - 1)
