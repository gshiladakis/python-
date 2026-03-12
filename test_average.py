# This program promots the user to enter three test
# scores. It displays the average of those scores
# and congratulates the user if the average is 95
# or greater.

def main():
    # Get the three test scores.
    test1 = input('Enter the score for test 1: ')
    test2 = input('Enter the score for test 2: ')
    test3 = input('Enter the score for test 3: ')

    # Calculate the average test score.
    average = (test1 + test2 + test3) /  3.0

    # Print the average
    print('The averager score is', average)

    # If the average is 95 or greater, 
    # congratulate the user.
    if average >= 95:
        print('Congratulations!)
        print('That is a great average!')

# Call the main function.
main()
