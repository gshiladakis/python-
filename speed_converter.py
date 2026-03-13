# This program converts the speeds 60 kph
# through 130 kph (in 10 kph increments)
# to mph.

def main():
    # Print the table headings.
    print('kph\tmph')
    print('-----------------')

    # Print the speeds.
    for kph in range(60, 131, 10):
        mph = kph * 0.6214
        print(kph, '\t', mph)

# Call the main function.
main()
