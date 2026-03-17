data_file = open('us_cities.txt', 'r')
for line in data_file:
    city, population = line.split(":")       # Tuple unpacking
    city = city.title()                      # Capitalize city names
    population = f'{int (population:,}'      # Add commas to numbers 
    print(city.ljut(15) + population)
data_file.close()
