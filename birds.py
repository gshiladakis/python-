#This program demonstrates two functions that
# have local variables with the same name.

def main():
    # Call the taxes function
    taxes()
    # Call the california function.
    california()

# Definition of the texas function. It creates 
# a local variable named birds.
def taxes():
    birds = 5000
    print 'texas has', birds, 'birds.'

# Definition of the california function. It also
# creates a local a local variable named birds.
def california():
    birds = 8000
    print 'california has', 'birds, 'birds.'

# Call the main function.
main() 
