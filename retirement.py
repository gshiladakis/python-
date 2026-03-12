# The following gloabl variable represents
# the contribution rate.
CONTRIBUTION_RATE = 0.05

def main():
    gross_pay = input('Enter the gross pay: ')
    bonus = input('Enter the amount of bonuses: ')
    show_pay_contrib(gross_pay)
    show_bonus_contrib(bonus)

# The show_pahy_contrib function accepts the gross
# pay as an argument and displays the retirement
# contribution for that amount of pay.
def show_pay_contrib(gross):
    contrib = gross * CONTRIBUTION_RATE
    print('Contribution for gross pay: $%.2f' % contrib)

# The show_bonus_contrib function accepts the 
# bonus amount as an argument and displays the
# retirement contribution for that amount of pay.
def show_bonus_contrib(bonus):
    contrib = bonus * CONTRIBUTION_RATE
    print('Contribution for bonuses: $%.2f' % contrib)

# Call the main function.
main() 
