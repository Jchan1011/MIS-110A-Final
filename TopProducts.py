# -*- coding: utf-8 -*-
"""

"""
def topProducts():
    import seaborn as sns 
    import pandas as pd    
    import numpy as np
    import matplotlib.pyplot as plt
    xl = pd.ExcelFile("FA18SalesData.xlsx")
    SalesData = xl.parse("Orders")
    
    lines = "="*25  
    
    product_sale = SalesData[["Sub-Category", "Sales", "Segment"]]
    
    print(lines)
    print("Sub-Category by Sales and Segment")
    print("For a type of customer, show the most/least popular selling sub-categories")
    print(lines)
    
    flag1 = True
    flag2 = True
    #1st input loop
    while flag1:
        top10 = input("Sort Sub-Categories by Sales by:\n1) Top 10 in sales\n2) Last 10 in sales\nEnter a number to select: ")
        if top10 == "1":
            flag1 = False
        elif top10 == "2":
            flag1 = False
        else:    
            print("Sorry, that was an invalid menu option. Please enter 1 or 2 to select a menu option.")
            continue
        #2nd input loop
        while flag2:
            segment_chosen = input("Select the type of customers to analyze:\n1) Consumer\n2) Corporate\n3) Home Office\nEnter a number to select: ")
            if segment_chosen == "1":
                segment = "Consumer"
                flag2 = False
            elif segment_chosen == "2":
                segment = "Corporate"
                flag2 = False
            elif segment_chosen == "3":
                segment = "Home Office"
                flag2 = False        
            else:    
                print("Sorry, that was an invalid menu option. Please enter 1, 2, or 3 to select a menu option.")
                continue
        print(lines)
        #display sub-categories
        product_salesum = product_sale.loc[product_sale["Segment"]==segment]
        popular_subcategory = product_salesum.groupby("Sub-Category").sum().sort_values(by="Sales", ascending = False)
        if top10 == "1":
            print("\nThe top 10 most popular sub-categories for " + segment + " customers are: ")            
            print(popular_subcategory.head(10))
        elif top10 == "2":
            print("\nThe 10 least popular sub-categories for " + segment + " customers are: ")
            print(popular_subcategory.tail(10))
        else:
            print("Please try again.")
        print("\n")
        print(lines)
    
    #create dataframe for barchart
    ProductSales = SalesData[["Sub-Category", "Sales", "Segment"]]
    if top10 == "1":
        ProductSalesSum=ProductSales.loc[ProductSales["Segment"]==segment].groupby(by="Sub-Category").sum().sort_values(by="Sales", ascending = False).head(10)
        print("\nSales for Top 10 Sub-Categories for " +segment+ " customers")
    elif top10 == "2":
        ProductSalesSum=ProductSales.loc[ProductSales["Segment"]==segment].groupby(by="Sub-Category").sum().sort_values(by="Sales", ascending = False).tail(10)
        print("\nSales for Last 10 Sub-Categories for " +segment+ " customers")
    ProductSalesSum = ProductSalesSum.reset_index()    
        
    #make the barchart
    barchart1 = sns.barplot(x="Sales", y= "Sub-Category", data=ProductSalesSum)
    barchart1.set_title("" +segment+ " Sales by Sub-Category")
    
    #set palette and hues
    sns.set(style="whitegrid", color_codes=True)
    pal = sns.color_palette("Blues_d", len(ProductSalesSum))
    rank = ProductSalesSum["Sales"].argsort().argsort() 
    sns.barplot(x='Sales',y='Sub-Category',data=ProductSalesSum, palette=np.array(pal[::-1])[rank])
    plt.show()