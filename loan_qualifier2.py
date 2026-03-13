# THis program determines whether a bank customer
# qualifies for a loan.

def main():
    # Get the customer's annual salary.
    salary = input('Enter your anjual salary: ')
  
    # Get the number of years on the current job.
   year_on_job = input('Enter the number of ' + \
                        'years on your current_job: ')

    # Determine whether the customer qualifies.
    if salary >= 30000.0 and years_on_job >= 2:
       print('You qualify for the loan.')
    else:
         print('You do not qualify for this loan.')
      
  # Call the main function.
  main()
