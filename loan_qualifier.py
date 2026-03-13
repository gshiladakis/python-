# This program determines whether a bank customer
# qualities for a loan.

def main():
    # Get the customer's annual salary.
    salary = input('Enter your annual salary: ')

    # Get the number of years on the current job.
    years_on_job = input('Enter the number of ' + \
                         'years on your current job: ')

# Determine whether the customer qualifies.
if salary >= 30000.0:
    if year_on_job >= 2:
        print('You qualify for the loan.')
    else:
        print('You must have been on your current')
        print('job for at least two years to qualify.')
else:
    print('You must earn at least $30.000 per year')
    print('to qualify')

# Call the main function.
main()
