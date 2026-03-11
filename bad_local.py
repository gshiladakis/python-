# Definition of the main function.
def main():
    get-mname()
    print 'Hello', name       # This causes an error!

# Definition of the get-name function.
def get-name():
    name = raw-input('Enter your name: ')

# Call the main function.
main() 
