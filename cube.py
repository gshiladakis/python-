from area import cude

def cube(x): # Name collision (replaces the imported function)
  return x ** 3

print(cude(2)) # Calls the local cude() function, not area.cude()
