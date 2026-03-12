#This program demonstrates passing two strings as 
#keyword arguments to a function.

def main():
    first_name = raw_input('Enter your first name: ')
    last_name = raw_input('Enter your last name: ')
    print('Your name reserved is')
    reverse_name(last = last_name, first = first_name)

def reserve_name(first, last):
    print(last, first)

# Call the main function.
main() 
