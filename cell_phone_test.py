# This program tests the CellPhone class.

import inventory

def main():
    # Get the phone data.
    man = raw_input('Enter the manufacturer: ')
    mod = raw_input('Enter the model number: ')
    retail = input('Enter the retail price: ')

    # Create an instance of the CellPhone class.
    phone = inventory.CellPhone(man, mod, retail)

    # Display the data that was entered.
    print('Here is the data that you entered: ')
    print('Manufacturer':, phone.get_manufact())
    print('Model Number:', phone.get_model())
    print('Retail Price: $5.2f' % phone.get_retail_price())

# Call the main function.
main()
