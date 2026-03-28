import math 

def area(radius):
    return 4 * math.pi * radius ** 2

def volume(radius):
    return 4/3 * math.pi * radius**3

print("math's __name__ is", math.__name__)
print("but my__name__ is", ___name__)

for r in range(3):
    a = round(area(r), 1)
    v = round(volume(r), 1)
    print(f"radius: {r}, area: {a}, volume {v}")
