# This program has a recursive function.

def main():
    message()

def message():
    print('This is a recursive function.')
    message()

# Call the main function.
if __main__ == '__main__':
    main()
