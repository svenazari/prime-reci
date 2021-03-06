#Verison 2.1
#Requirements: Python3
#Version 2.1 checks if number is prime and then calculates how many digits is in period of decimal expansion of prime numbers.
#Made by Sven Azari
#http://www.github.com/svenazari

#imports
import math
from os import system, name
from itertools import count

#clear
def clear ():
  if name == 'nt':
      _ = system('cls')
  else:
      _ = system('clear')

#main part
def primetest ():
    print ("####################")
    print ("#                  #")
    print ("#    PRIME RECI    #")
    print ("#                  #")
    print ("####################")
    print (" ")
    xs = input ("X = ")
    if xs == "exit" or xs == "EXIT":
      clear()
      exit()
    else:
      x = float(xs)
    print (" ")
    x1 = math.ceil(x / 2) + 1
    if x == 1:
      print ("NOR PRIME NOR COMPOSIT")
      fuex ()
    elif x == 2:
      print ("PERIOD OD DECIMAL EXPANSION IS FINITE")
      fuex ()
    elif x < 1:
      print ("ENTER ONLY NATURAL NUMBERS")
      primetest ()
    for PT in range (2, x1, 1):
        a = x % PT
        if a == 0:
            break
    if a != 0:
        li = [] #list for comparisong
        d = 1
        c = 0 #number of itirations

        while True: #calculation loop
            o = d % x
            try:
                b = li.index(o)
            except ValueError:
                li.append(o)
                d = o * 10
                c +=1
            else:
                break
        
        print ("PERIOD OD DECIMAL EXPANSION")
        print (c) #final print of length of period of decimal expansion
        print (" ")
        fuex ()

    else:
        print ("INPUTED NUMBER IS NOT PRIME")
        print (" ")
        fuex ()

#exit function
def fuex ():
  ex = float(input ("[1 (new), 2 (exit)]: "))
  if ex == 1:
    clear ()
    primetest ()
  elif ex == 2:
    clear ()
    exit ()
  else:
    print ("Wrong input!")
    fuex ()

clear ()
primetest ()
