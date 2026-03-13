# This program imports the simulation module and
# creates three instances of the Coin class.

import simulation

def main():
    # Create three objects from the Coin class.
    coin1 = simulation.Coin()
    coin2 = simulation.Coin()
    coin3 = simulation.Coin()

   # Display the side of each coin that is facing up.
   print('I have three coin with these sides up:')
   print(coin1.get_sideup())
   print(coin2.get_sideup())
   print(coin3.get_sideup())
   print

  # Toss the coin.
  print('I am tossing all three coins..')
  print
  coin1.toss()
  coin2.toss()
  coin3.toss()

  # Display the side of each coin that is facing up.
  print('Now here are the sides that are up:')
  print(coin1.get_sideup())
  print(coin2.get_sideup())
  print(coin3.get_sideup())
  print

# Call the main function.
main() 
