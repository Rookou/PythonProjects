#imports
import time
import math

#Dictionaries

temps = {
  "Perth City": 40.5,
  "Ellenbrook": 41.1,
  "Joondalup": 39.8,
  "The Vines": 42.0,
  "Aveley": 40.0
}
  
#definitions

def Alltemp():
  for i, b in temps.items():
    time.sleep(.5)
    print(i, b)
  time.sleep(2)
  return main()

def Hightemp():
  print("Maximum Temperature")
  print(" ")
  tempmaxplace = max(zip(temps.values(), temps.keys()))[1]
  tempmax = (max(temps.values()))
  print(tempmaxplace + ":", tempmax)
  time.sleep(.5)
  print("-----------------------------------")
  time.sleep(1.5)
  return main()

def Lowtemp():
  print("Minimum Temperature")
  print(" ")
  tempminplace = min(zip(temps.values(), temps.keys()))[1]
  tempmin = (min(temps.values()))
  print(tempminplace + ":", tempmin)
  time.sleep(.5)
  print("-----------------------------------")
  time.sleep(1.5)
  return main()

def Comptemp():
  City1 = input("Enter the first city you want to compare: ")
  if City1 not in temps.keys():
    print("Invalid city, please try again")
    return Comptemp()
  City2 = input("Enter the second city you want to compare: ")
  if City2 not in temps.keys():
    print("Invalid city, please try again")
    return Comptemp()
  print(City1 + ":", temps[City1])
  time.sleep(1)
  print(City2 + ":", temps[City2])
  time.sleep(1.5)
  print("-----------------------------------")
  return main()

def Changetemp():
  choice = input("What city's temperature would you like to change? ")
  if choice in temps.keys():
    new_temp = float(input("What is the new temperature? "))
    rounded_num = f'{round(new_temp,1)}'
    temps[choice] = rounded_num
    print("Temperature updated successfully.")
    time.sleep(2)
  else:
    print("Invalid city, please try again.")
    time.sleep(1.5)
    return Changetemp()
  return main()

def main():
  print("-----------------------------------")
  print("1. Display all temperatures")
  print("2. Show highest temperature")
  print("3. Show lowest temperature")
  print("4. Compare temperatures of each city")
  print("5. Change temperature of a city")
  print("-----------------------------------")
  select = input("Enter number 1 - 5: ")
  print("-----------------------------------")
  if select == "1":
    return Alltemp()
  elif select == "2":
    return Hightemp()
  elif select == "3":
    return Lowtemp()
  elif select == "4":
    return Comptemp()
  elif select == "5":
   return Changetemp()
  else:
    print("Invalid answer, please try again")
    time.sleep(2)
    print("-----------------------------------")
    return main()

#code
main()