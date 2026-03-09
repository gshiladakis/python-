# Person class
class Person:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = adress
        self.phone = phone

    def display_person(self):
        print("Name:", self.name)
        print("Address:", self.address)
        print("Phone:", self.phone)

# Customer class (subclass of Person)
class Customer(Person):
    def __init__(self, name, address, phone, customer_number, mailing_list):
        # Call the parent class constructor
        Person.__init__(self, name, address, phone)

        self.customer_number = customer_number
        self.mailing_list = mailing_list

    def display_customer(self):
        self.display_person()
        print("Customer Number:", self.customer_number)
        print("Mailing List:", self.mailing_list)

# Demonstrate program
def main():
    # Create a Customer object
    customer1 = Customer(
        "Sarah Johnson",
        "123 Main Street",
        "555-1234",
        1001,
        True
    )

    # Dsiplay the customer information
    print("Customer Information:")
    customer1.display_customer()

# Run the program
main() 
