# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 20:13:26 2018

@author: Jeffrey
"""
def RegionMenu():
    import pandas as pd
    xl = pd.ExcelFile("FA18SalesData.xlsx")
    SalesData = xl.parse("Orders") 
       
    lines = "="*25  
    
    flag1 = True
    flag2 = True
    flag3 = True
    flag5 = True
       
    while flag1:
       while flag5: 
            print ("""
                           Welcome to the region menu\n
                             \n 1: Central 
                             \n 2: South
                             \n 3: East 
                             \n 4: West
                             \n 5: All
                             \n 6: Go Back """
                            # \n 7: Quit
                                             )
            #Go Back is to go back to group menu 
            selection = input("Please enter the number corresponding to your choice: ")
        
            print(lines)
            flag2 = True
            flag3 = True
            while flag2:
                if selection == "1":
                     region = "Central"
                     flag2 = False
                     flag1 = False
                elif selection == "2":
                     region = "South"
                     flag2 = False
                     flag1 = False
                elif selection == "3":
                     region = "East"
                     flag2 = False
                     flag1 = False
                elif selection == "4":
                     region = "West"
                     flag2 = False
                elif selection == "5":
        #ALL REGIONS
                     flag2 = False
                     
                     print ("""\nData pertaining to all regions
                            \n 1: Quantity of sales
                            \n 2: Most profit 
                            \n 3: Technology 
                            \n 4: Furniture
                            \n 5: Office Supplies
                            \n 6: Go Back """ )
                         #   \n 7: Quit  )
                     
                     selection = input("Please enter the number corresponding to your choice: ")
                     
                     keep_going = True
                     while keep_going:
                     
                         if selection == "1":
                             #Quantity of sales for all regions
                             region_quantity_cols = SalesData[["Region", "Quantity"]]
                             region_purchases = region_quantity_cols.groupby(by="Region").sum().sort_values(by="Quantity", ascending = False)
                             print(region_purchases.head(4))
                    
                    
                             go = True
                             repeat = True
                             while go:
                                 while repeat:
                                     print (""" \n Would you like to return region menu
                                            \n1. Yes 
                                            \n2. No
                                                """)
                               
                                        
                                     choice = input("Please enter the number corresponding to your choice: ")
                                     if choice == "1":
                                        go = False
                                        keep_going = False 
                                        repeat = False
                                     elif choice == "2":
                                        go = False
                                        keep_going = False
                                        repeat = False
                                        flag1 = False
                                        flag5 = False
                                     else:
                                        print ("Unkown number selected, please try again")
                                        continue
                                        
                         
                         elif selection == "2":
                    #profit from all regions
                            region_profits = SalesData[["Region", "Profit"]]
                            region_total_profits = region_profits.groupby(by="Region").sum().sort_values(by="Profit", ascending = False)
                            print(region_total_profits.head(4))
                    
                            repeat = True
                            go = True
                            while go:
                                while repeat:
                                 print (""" \n Would you like to return region menu
                                        \n1. Yes
                                        \n2. No
                                            """)
                           
                    
                                 choice = input("Please enter the number corresponding to your choice: ")
                                 if choice == "1":
                                    go = False
                                    keep_going = False 
                                    repeat = False
                                 elif choice == "2":
                                    go = False
                                    keep_going = False
                                    repeat = False
                                    flag1 = False
                                    flag5 = False
                                 else:
                                    print ("Unkown number selected, please try again")
                                    #repeat = False
                         
                         elif selection == "3":
                    #Technology from all regions
                            region_technology = SalesData[["Region", "Category", "Quantity"]]
                            region_total_technology = region_technology.loc[SalesData["Category"]=="Technology"].groupby(by="Region").sum().sort_values(by = "Quantity", ascending = False)
                            print(region_total_technology.head(4))
                      
                            repeat = True
                            go = True
                            while go:
                                while repeat:
                                    print (""" \n Would you like to return region menu
                                            \n1. Yes
                                            \n2. No
                                                """)
                               
                        
                                    choice = input("Please enter the number corresponding to your choice: ")
                                    if choice == "1":
                                        go = False
                                        keep_going = False
                                        repeat = False
                                    elif choice == "2":
                                        go = False
                                        keep_going = False
                                        repeat = False
                                        flag1 = False
                                        flag5 = False
                                        
                                    else:
                                        print ("Unkown number selected, please try again")
                                        #repeat = False
                                        continue
                
                         elif selection == "4":
                    #Furniture
                            region_furniture = SalesData[["Region", "Category", "Quantity"]]
                            region_total_furniture = region_furniture.loc[SalesData["Category"]=="Furniture"].groupby(by="Region").sum().sort_values(by = "Quantity", ascending = False)
                            print(region_total_furniture.head(4))
                            
                            repeat = True
                            go = True
                            while go:
                                while repeat:
                                 print (""" \n Would you like to return region menu
                                        \n1. Yes
                                        \n2. No
                                            """)
                           
                    
                                 choice = input("Please enter the number corresponding to your choice: ")
                                 if choice == "1":
                                    go = False
                                    keep_going = False 
                                    repeat = False
                                 elif choice == "2":
                                    go = False
                                    keep_going = False
                                    repeat = False
                                    flag1 = False
                                    flag5 = False
                                 else:
                                    print ("Unkown number selected, please try again")
                                    #repeat = False
                
                         elif selection == "5":
                    #Office Supplies
                          region_office_supplies = SalesData[["Region", "Category", "Quantity"]]
                          region_total_office_supplies = region_office_supplies.loc[SalesData["Category"]=="Technology"].groupby(by="Region").sum().sort_values(by = "Quantity", ascending = False)
                          print("Office Supplies")
                          print(region_total_office_supplies.head(4))
                          
                          repeat = True
                          go = True
                          while go:
                              while repeat:
                                 print (""" \n Would you like to return region menu
                                        \n1. Yes
                                        \n2. No
                                            """)
                           
                    
                                 choice = input("Please enter the number corresponding to your choice: ")
                                 if choice == "1":
                                    go = False
                                    keep_going = False 
                                    repeat = False
                                 elif choice == "2":
                                    go = False
                                    keep_going = False
                                    repeat = False
                                    flag1 = False
                                    flag5 = False
                                 else:
                                    print ("Unkown number selected, please try again")
                                    #repeat = False
                         
                         elif selection == "6":
                             #supposed to return to main region menu 
                             keep_going = False
                      #   elif selection == "7":
                             #quit
                        #     keep_going = False
                         #    flag1 = False
                        #     flag2 = False
                          #   flag5 = False
                         else:
                             print ("Unknown option selected, please try again")
                             break
                     flag2 = False
                     break
         #END OF ALL REGIONS
                elif selection == "6":
                      return "\n"
            #    elif selection == "7":
                #     flag2 = False
            #         flag1 = False
             #        flag5 = False
            #         break
                else:
                    print ("Unkown number selected, please try again")
                    flag2 = False
                    keep_going = False
                    continue
            
            
         #SINGLE REGIONS
                while flag3:
                    print ("\nData pertaining to " + region +
                                
                               """    
                                      \n 1: Quantity of Sales
                                      \n 2: Most Profit 
                                      \n 3: Category Sales
                                      \n 4: Category Profits
                                                   """)
                    pick = input("Please enter the number corresponding to your choice: ")
                    #Quantity of Sales    
                    if pick == "1":
                        product_sale = SalesData[["Sub-Category", "Sales", "Region"]]
                        north_salesum = product_sale.loc[product_sale["Region"]== region]
                        north_saletotal = north_salesum.groupby("Sub-Category").sum().sort_values(by="Sales", ascending = False)
                        print(region)
                        print(north_saletotal)
                        
                        go = True
                        while go:
                            print (""" \n Would you like to return to region menu
                               \n1. Yes
                               \n2. No
                                   """)
                               
                        
                            choice = input("Please enter the number corresponding to your choice: ")
                            if choice == "1":
                                go = False
                                flag3 = False
                                flag2 = True
                                
                            elif choice == "2":
                                go = False
                                flag1 = False
                                flag3 = False
                                flag5 = False
                            else:
                                print ("Unkown number selected, please try again")
                                
                     
                    #Most Profit
                    elif pick == "2":
                        product_sale = SalesData[["Sub-Category", "Profit", "Region"]]
                        north_profitsum = product_sale.loc[product_sale["Region"]== region]
                        north_profit_total = north_profitsum.groupby("Sub-Category").sum().sort_values(by="Profit", ascending = False)
                        print(region)
                        print(north_profit_total)
                        
                        go = True
                        while go:
                            print (""" \n Would you like to return region menu
                               \n1. Yes
                               \n2. No
                                   """)
                               
                        
                            choice = input("Please enter the number corresponding to your choice: ")
                            if choice == "1":
                                go = False  
                                flag3 = False
                            elif choice == "2":
                                go = False
                                flag1 = False
                                flag3 = False
                                flag5 = False
                                
                            else:
                                print ("Unkown number selected, please try again")
                                continue
                    #Category Sales
                    elif pick == "3":
                        product_sale = SalesData[["Category", "Sales", "Region"]]
                        north_category_sum = product_sale.loc[product_sale["Region"]== region]
                        north_category_total = north_category_sum.groupby("Category").sum().sort_values(by="Sales", ascending = False)
                        print(region)
                        print(north_category_total)
                        
                        go = True
                        while go:
                            print (""" \n Would you like to return region menu
                               \n1. Yes
                               \n2. No
                                   """)
                               
                        
                            choice = input("Please enter the number corresponding to your choice: ")
                            if choice == "1":
                                go = False 
                                flag3 = False
                            elif choice == "2":
                                go = False
                                flag1 = False
                                flag3 = False
                                flag5 = False
                            else:
                                print ("Unkown number selected, please try again")
                                continue
                    #Category Profit
                    elif pick == "4":
                        product_sale = SalesData[["Sub-Category", "Profit", "Region"]]
                        north_category_sum = product_sale.loc[product_sale["Region"]== region]
                        north_category_total = north_category_sum.groupby("Sub-Category").sum().sort_values(by="Profit", ascending = False)
                        print(region)
                        print(north_category_total)
                        
                        go = True
                        while go:
                            print (""" \n Would you like to return region menu
                               \n1. Yes
                               \n2. No
                                   """)
                               
                        
                            choice = input("Please enter the number corresponding to your choice: ")
                            if choice == "1":
                                go = False
                                flag3 = False
                            elif choice == "2":
                                go = False
                                flag1 = False
                                flag3 = False
                                flag5 = False
                            else:
                                print ("Unkown number selected, please try again")
                                continue
         #           elif pick == "5":
          #              flag1 = False
          #              flag3 = False
          #              flag5 = False
                    else:
                        print ("Unkown number selected, please try again")
                        continue 
            
                break            
    
            
       
    
