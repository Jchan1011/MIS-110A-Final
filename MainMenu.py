# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 19:23:47 2018

@author: Don
"""
#import seaborn as sns 
#import pandas as pd    
#import numpy as np
#import matplotlib.pyplot as plt

from LoginandRegistration import registration, login
from TopProducts import topProducts
from MostBought import mostBought
from RegionMenu import RegionMenu
from LostProfit import lostProfit

#xl = pd.ExcelFile("FA18SalesData.xlsx")
#SalesData = xl.parse("Orders")

#function is used at end of each insight to let user use function again or return to main menu
def returnMenu():
    while choosing:
        global stillUse
        tryAgain = input("Would you like to \n1) Start over \n2) Return to the Main Menu\n\nEnter a number to select: ")
        if tryAgain == "1":
            #usingFn = True
            stillUse = True
            break
        if tryAgain == "2":
            #usingFn = False
            stillUse = False
            break
        else:
            print("Sorry, that was an invalid menu option. Please enter a number to select.")

lines = "="*25  
print("="*10 + "[ User Login ]" + "="*10)
login() 

#when login successful
print("Welcome to the Main Menu\n")

#flags for while loops
loggedIn = True
global usingFn
usingFn = True
global stillUse
stillUse = True
choosing = True

while loggedIn:
    loggedIn = True
    print("\n" + "="*10 + "[ Main Menu ]" + "="*10)
    menu = input("""   
   ===[ Business Insights ]===
   
    1) View Product Sales by Customer Segment
    2) View Discount Profit-Loss
    3) View Region Insights
    4) View Top Buying Customers by Year
    
        ===[ Account ]===
        
    5) Register a new user
    6) Logout
    7) Exit      

Enter a number to select a menu option: """)
    
    while usingFn:

        #top products subcategories
        if menu == "1":
            topProducts()
            returnMenu()
            if stillUse == True:
                continue
            elif stillUse == False:
                break
        
        #discount profit loss
        if menu == "2":
            lostProfit()
            returnMenu()
            if stillUse == True:
                continue
            elif stillUse == False:
                break
        
        #region data
        if menu == "3":
            RegionMenu()
            returnMenu()
            if stillUse == True:
                continue
            elif stillUse == False:
                break
        
        #customers who bought the most of a subcat in a year
        if menu == "4":
            mostBought()
            returnMenu()
            if stillUse == True:
                continue
            elif stillUse == False:
                break
        
        #register a new user
        elif menu == "5":
            registration() 
            break
        
        #logout and return to login menu
        elif menu == "6":
            print("Logging out...\n")
            loggedIn = False
            print("="*10 + "[ User Login ]" + "="*10)
            login() 
            loggedIn = True #when login is successful, flag is set back to True
            print("Welcome to the Main Menu\n")
            break #and then redo main menu
        
        #exit program and close
        elif menu == "7":
            print(lines)
            print("\nExiting program.\n")
    #            conn.close()
            loggedIn = False #the main while loop will stop running
            break
        
        else:
            print("Sorry, that was an invalid menu option. Please enter a number to select a menu option.")
            break

