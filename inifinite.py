# This program demonstrates an infinite loop.
def main():
    # Create a variable to control the loop.
    keep_going = 'y'

    # Warning! Infinite loop!
    while keep_going == 'y':
        # Get a salesperson's sales and commission rate.
        sales = input('Enter the amount of sales: ')
        corm_rate = input('Enter the commission rate: ')

       # Calcualte the commission.
       commission = sales * comm_rate

       # Display the commission.
       print('The commission is $%.2f.' % commission) 

# Call the main function.
main() 
