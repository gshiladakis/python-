def tax(total):
  return .06 * total

def auto_tip(total):
    return  .2 * total

bill = 100.0
bill += tax(bill) + auto_tip(bill)
