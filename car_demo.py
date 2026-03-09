# This program demonstrates the Car class.

import vehicles

def main():
    # Create an object from the Car class.
    # The car is a 2007 Audi with 12,500 miles, priced
    # at $21,500,00 and has 4 doors.
    used_car = vehicle.Car('Audi', 2007, 12500, 21500.0, 4)

    # Display the car's data.
    print('Make:', used_car.get_make())
    print('Model:', used_car.get_model())
    print('Mileage:', used_car.get_mileage())
    print('Price:', used_car.get_price())
    print('Number of doors:', used_car.get_doors())

# Call the main function.
if _ _name_ _ == '__main_ _':
    main()




















































# The Truck class represents a pickup truck. It is a 
# subclass of the Automobile class.

class Truck(Automobile):
  # The __init__ method accepts arguments for the 
  # Truck's make, model, mileage, price, and drive type.

  def __init__(self, make, model, mileage, price, drive_type):
      # Call the superclass's __Init__ method and pass
      # the required arguments. Note that we also have
      # to pass self as an argument.
      Automobile.__init__(self, make, model, mileage, price)

      # Initia;ize the __drive__type attribute. 
      self.__drive_type = drive_type

   # The set_drive_type method is the mutator for the 
   # __drive_type attribute.

  def set_drive_type(self, drive_type):
    self.__drive = drive_type

  # The get_drive_type method is the accessor for the 
  # __drive_type attribute.

  def get_drive_type(self):
      return self.__drive_type

# The SUV class represents a sport utility vehicle. It
# is a subclass of the Automobile class.

class SUV(Automobile):
    # The __init__ method accepts arguments for the 
    # SUV's make, model, mileage, price, and passenger
    # capacity.

    def __init__(self, make, model, mileage, price, pass_cap):
        # Call the superclass's __init__ method and pass
        # the required arguments. Note that we also have
        # to pass self as an argument.
        Automobile.__init__(self, make, model, mileage, price)

        # Initialize the __pass_cap attribute.
        self.__pass_cap = pass_cap 

    # The set_pass_cap method is the mutator for the 
    # __pass_cap attribute.

    # def set_pass_cap(self, pass_cap):
          self.__pass_cap = pass_cap

    # The get_pass_cap method is the accessor for the 
    # __pass_cap attrbute.

    def get_pass_cap(self):
        return self.__pass_cap 
