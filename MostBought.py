# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 12:19:22 2018

@author: cobuser


"""


def mostBought():
    import pandas as pd
    xl = pd.ExcelFile("FA18SalesData.xlsx")
    SalesData = xl.parse("Orders")
    
    lines = "="*25  
    print(lines)
    print("Top Buying Customers of the Year for a Product Sub-Category")
    print("For a sub-category of product, show the customers who bought the most in a specific year")
    print(lines)
    
    SalesDataYear = SalesData
    SalesDataYear['Year']=SalesDataYear["Order Date"].dt.year
    #SalesDataYear['Year']=SalesDataYear["Order Date"].dt.year
    
    
    
    
    #YearlyQuantity = SalesDataYear[["Customer Name", "Sub-Category", "Quantity", "Year"]]
    #YearlyQuantitySum=YearlyQuantity.groupby(by="Year").sum()
    #YearlyQuantitySum = YearlyQuantitySum.reset_index()
    
    #idea isolate to specific year
    #
    #
    #year = SalesData.Year.unique()
    
    
    flag1 = True
    flag2 = True
    while flag1:
        subcat_chosen = input("""Choose a sub-category: 
            1) Accessories
            2) Appliances
            3) Art
            4) Binders
            5) Bookcases
            6) Chairs
            7) Copiers
            8) Envelopes
            9) Fasteners
            10) Furnishings
            11) Labels
            12) Machines
            13) Paper
            14) Phones
            15) Storage
            16) Supplies
            17) Tables
            Enter a number to select: """)
        if subcat_chosen == "1":
            subcat = "Accessories"
            flag1 = False
        elif subcat_chosen == "2":
            subcat = "Appliances"
            flag1 = False
        elif subcat_chosen == "3":
            subcat = "Art"
            flag1 = False        
        elif subcat_chosen == "4":
            subcat = "Binders"
            flag1 = False
        elif subcat_chosen == "5":
            subcat = "Bookcases"
            flag1 = False    
        elif subcat_chosen == "6":
            subcat = "Chairs"
            flag1 = False
        elif subcat_chosen == "7":
            subcat = "Copiers"
            flag1 = False        
        elif subcat_chosen == "8":
            subcat = "Envelopes"
            flag1 = False
        elif subcat_chosen == "9":
            subcat = "Fasteners"
            flag1 = False    
        elif subcat_chosen == "10":
            subcat = "Furnishings"
            flag1 = False
        elif subcat_chosen == "11":
            subcat = "Labels"
            flag1 = False        
        elif subcat_chosen == "12":
            subcat = "Machines"
            flag1 = False
        elif subcat_chosen == "13":
            subcat = "Paper"
            flag1 = False    
        elif subcat_chosen == "14":
            subcat = "Phones"
            flag1 = False
        elif subcat_chosen == "15":
            subcat = "Storage"
            flag1 = False        
        elif subcat_chosen == "16":
            subcat = "Supplies"
            flag1 = False
        elif subcat_chosen == "17":
            subcat = "Tables"
            flag1 = False    
        else:    
            print("Sorry, that was an invalid menu option. Please enter a valid number to select.")
            continue
            
        while flag2:
            year_chosen = input("Choose the year to view top customers: \n1) 2014\n2) 2015\n3) 2016\n4) 2017\nEnter a number to select: ")
            if year_chosen == "1":
                year = 2014
                flag2 = False
            elif year_chosen == "2":
                year = 2015
                flag2 = False
            elif year_chosen == "3":
                year = 2016
                flag2 = False        
            elif year_chosen == "4":
                year = 2017
                flag2 = False
            else:    
                print("Sorry, that was an invalid menu option. Please enter a valid number to select.")
                continue
        print(lines)
        
    subcat_quantity = SalesDataYear[["Customer Name", "Sub-Category", "Quantity", "Year"]]
    MostBought = subcat_quantity.loc[subcat_quantity["Sub-Category"]==subcat]
    MostBoughtYear = MostBought.loc[MostBought["Year"]==year].groupby(by="Customer Name").sum().sort_values(by="Quantity", ascending = False)
    
    
    total_customers = MostBoughtYear.shape
    
    print("\nThe total quantity of " + subcat + " sold in " +str(year)+ " is: " + str(total_customers[0]))
    print("Top 30 customers for " +subcat+ ": ")
    print(MostBoughtYear.loc[:,["Quantity"]].head(30))
    #print(MostBoughtYear.columns.values)
    #https://stackoverflow.com/questions/10665889/how-to-take-column-slices-of-dataframe-in-pandas
    