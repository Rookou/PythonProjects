#imports
import time
import math

#start code

ttlcost = 0
order = {}

#Functions

#Final pay screen and customisations

def payandcustomisations():
    print("Would you like to make any customisations for $2 Y/N")
    customisation = input(" ")
    if customisation.upper() == "Y":
      od = "Customisations cost"
      order[od] = 2.00
      global ttlcost
      ttlcost = ttlcost + 2
      print("What would you like to change?")
      global costumitems
      customitems = input(" ")
      print("The total comes to", '%.2f' % ttlcost ) 
    elif customisation.upper() == "N":
      print("The total comes to", '%.2f' % ttlcost )
    else:
      print("That was not a valid option")
      print("Returning to pay screen")
      time.sleep(1)
      payandcustomisations()
      

      
#Final review before paying

def review():
  print("Your order is")
  for i in order:
    print(i+":", order[i])
    time.sleep(1)
  print("The current total is", '%.2f' % ttlcost )
  print("Press 1 to continue")
  print("Press 2 to restart order")
  continuationnumb = int(input(" "))
  if continuationnumb == 1:
     payandcustomisations()
  elif continuationnumb == 2:
    reset()
  else:
    print("That was not an option")
    print("Returning to review")
    review()            

#Reset the order

def reset():
  dict.clear(order)
  ttlcost = 0
  orderscreen()
  
# All the different choice codes 
  
def choice1():
  print('You have chosen Steak')
  global order
  od = "Steak"
  order[od] = 25.99
  global ttlcost
  ttlcost = ttlcost + 25.99
  print("Press 1 to continue")
  print("Press 2 to order more")
  fwd = int(input(" "))
  if fwd == 1:
    review()
  elif fwd == 2:
    orderrev()
  else:
    print("Invalid Option")
    return

def choice2():
  print('You have chosen Chicken Schnitzel')
  global order
  od = "Chicken Schnitzel"
  order[od] = 22.95
  global ttlcost
  ttlcost = ttlcost + 22.95
  print("Press 1 to continue")
  print("Press 2 to order more")
  fwd = int(input(" "))
  if fwd == 1:
    review()
  elif fwd == 2:
    orderrev()
  else:
    print("Invalid Option")
    return

def choice3():
  print('You have chosen Ribs')
  global order
  od = "Ribs"
  order[od] = 29.99
  global ttlcost
  ttlcost = ttlcost + 29.99
  print("Press 1 to continue")
  print("Press 2 to order more")
  fwd = int(input(" "))
  if fwd == 1:
    review()
  elif fwd == 2:
    orderrev()
  else:
    print("Invalid Option")
    return

def choice4():
  print('You have chosen Carbonara')
  global order
  od = "Carbaonara"
  order[od] = 19.99
  global ttlcost
  ttlcost = ttlcost + 19.99
  print("Press 1 to continue")
  print("Press 2 to order more")
  fwd = int(input(" "))
  if fwd == 1:
    review()
  elif fwd == 2:
    orderrev()
  else:
    print("Invalid Option")
    return

def choice5():
  print('You have chosen Trout')
  global order
  od = "Trout"
  order[od] = 20.15
  global ttlcost
  ttlcost = ttlcost + 20.15
  print("Press 1 to continue")
  print("Press 2 to order more")
  fwd = int(input(" "))
  if fwd == 1:
    review()
  elif fwd == 2:
    orderrev()
  else:
    print("Invalid Option")
    return

def choice6():
  print('You have chosen Gnocchi')
  global order
  od = "Gnocchi"
  order[od] = 10.55
  global ttlcost
  ttlcost = ttlcost + 10.55
  print("Press 1 to continue")
  print("Press 2 to order more")
  fwd = int(input(" "))
  if fwd == 1:
    review()
  elif fwd == 2:
    orderrev()
  else:
    print("Invalid Option")
    return

def choice7():
  print('You have chosen Pork Belly')
  global order
  od = "Pork Belly"
  order[od] = 23.95
  global ttlcost
  ttlcost = ttlcost + 23.95
  print("Press 1 to continue")
  print("Press 2 to order more")
  fwd = int(input(" "))
  if fwd == 1:
    review()
  elif fwd == 2:
    orderrev()
  else:
    print("Invalid Option")
    return

def choice8():
  print('You have chosen Chips')
  global order
  od = "Chips"
  order[od] = 7.99
  global ttlcost
  ttlcost = ttlcost + 7.99
  print("Press 1 to continue")
  print("Press 2 to order more")
  fwd = int(input(" "))
  if fwd == 1:
    review()
  elif fwd == 2:
    orderrev()
  else:
    print("Invalid Option")
    return

def choice9():
  print('You have chosen Coke')
  global order
  od = "Coke"
  order[od] = 3.95
  global ttlcost
  ttlcost = ttlcost + 3.95
  print("Press 1 to continue")
  print("Press 2 to order more")
  fwd = int(input(" "))
  if fwd == 1:
    review()
  elif fwd == 2:
    orderrev()
  else:
    print("Invalid Option")
    return

def choice10():
  print('You have chosen Water')
  global order
  od = "Water"
  order[od] = 0.00
  global ttlcost
  ttlcost = ttlcost + 0.00
  print("Press 1 to continue")
  print("Press 2 to order more")
  fwd = int(input(" "))
  if fwd == 1:
    review()
  elif fwd == 2:
    orderrev()
  else:
    print("Invalid Option")
    return
  
#The main code for ordering

def orderscreen():
  print("Enter 1 for Steak")
  print("Enter 2 for Chicken Schnitzel")
  print("Enter 3 for Ribs")
  print("Enter 4 for Carbonara")
  print("Enter 5 for Trout")
  print("Enter 6 for Gnocchi")
  print("Enter 7 for Pork belly")
  print("Enter 8 for Chips")
  print("Enter 9 for Coke")
  print("Enter 10 for Water")
  ordernum = int(input(" "))
  
  if ordernum == 1:
     choice1()
  elif ordernum == 2:
     choice2()
  elif ordernum == 3:
     choice3()
  elif ordernum == 4:
     choice4()  
  elif ordernum == 5:
     choice5()
  elif ordernum == 6:
     choice6()
  elif ordernum == 7:
     choice7()
  elif ordernum == 8:
     choice8() 
  elif ordernum == 9:
     choice9()
  elif ordernum == 10:
     choice10()    
  else:
    print('Sorry that is not a valid option')
    
#Review order after selecting add more to order

def orderrev():
  print("Your order is:")
  for i in order:
    print(i+":", order[i])
    time.sleep(1)
  print("The current total is", '%.2f' % ttlcost )
  print(" ")
  print("Press 1 to continue ordering")
  print("Press 2 to restart order")
  restartnumb = int(input(" "))
  if restartnumb == 1:
    print("What else would you like to order?") 
    print(" ")
    time.sleep(1)
    orderscreen()
  elif restartnumb == 2:
    reset()
  else:
    print("That was not an option")
    print("Returning to review")
    orderrev()                

#Menu

orderscreen()