def lostProfit():
    import pandas as pd
    import seaborn as sns
    import numpy as np
    import matplotlib.pyplot as plt
    import shutil
    
    xl = pd.ExcelFile("FA18SalesData.xlsx")
    SalesData = xl.parse("Orders")
    #Creates a column named "Lost-Profit" that calculates the dollar amount lost to discounts
    SalesData['Lost-Profit'] = SalesData.Sales/(1-SalesData.Discount) - SalesData.Sales
    SalesData['Year']=SalesData["Order Date"].dt.year
    
    columns = shutil.get_terminal_size().columns
    lines = "=".center(columns, '=')
    print(lines)
    print("=== [Discount Impact on Profits  by Subcategory] ===".center(columns))
    print("\nDisplays profit lost due to discounts and overall profitability of Sub-Categories".center(columns))
    print(lines)
    
    loopin = True
    while loopin:
        reset = ""
        filterColumnT1 = ""
        filterColumnT2 = ""
        topInput = ""
        while not filterColumnT2:
            chartfilter = input("Select an option to filter data:\n1) by Year \n2) by Region \n3) by Segment \nEnter a number to select:  ")
            if chartfilter == "1":
                while not filterColumnT1:
                    t2Input = input("Select a year:\n1) 2014 \n2) 2015 \n3) 2016 \n4) 2017 \nEnter a number to select:  ")
                    if t2Input == "1":
                        filterColumnT2 = 2014
                    elif t2Input == "2":
                        filterColumnT2 = 2015
                    elif t2Input == "3":
                        filterColumnT2 = 2016
                    elif t2Input == "4":
                        filterColumnT2 = 2017
                    else: 
                        print("Sorry, that was an invalid menu option.")
                        continue
                    filterColumnT1 = "Year"
            elif chartfilter == "2":
                while not filterColumnT1:
                    t2Input = input("Select a region:\n1) West \n2) Central \n3) South \n4) East  \nEnter a number to select:  ")
                    if t2Input == "1":
                        filterColumnT2 = "West"
                    elif t2Input == "2":
                        filterColumnT2 = "Central"
                    elif t2Input == "3":
                        filterColumnT2 = "South"
                    elif t2Input == "4":
                        filterColumnT2 = "East"
                    else: 
                        print("Sorry, that was an invalid menu option.")
                        continue
                    filterColumnT1 = "Region"
            elif chartfilter =="3":
                while not filterColumnT1:
                    t2Input = input("Select a segment:\n1) Consumer \n2) Corporate \n3) Home Office \nEnter a number to select:  ")
                    if t2Input == "1":
                        filterColumnT2 = "Consumer"
                    elif t2Input == "2":
                        filterColumnT2 = "Corporate"
                    elif t2Input == "3":
                        filterColumnT2 = "Home Office"
                    else:
                        print("Sorry, that was an invalid menu option.")
                        continue
                    filterColumnT1 = "Segment"
            else:
                print("Sorry, that was an invalid menu option. Please enter 1, 2, or 3 to select a menu option.")      
        while not topInput:
            try:
                strInput = input("Select # of Sub-Catergoies to Display (1-15):  ")
                if int(strInput) in range(1,16):
                    topInput = int(strInput)
                else: 
                    print("Sorry, that was an invalid menu option. Please enter a number between 1 and 15.")
                    continue
                break
            except ValueError:
                print("Sorry, that was an invalid menu option. Please enter a number between 1 and 15.")
            continue
    
    
        dfT1 = SalesData[["Sub-Category","Lost-Profit","Profit", filterColumnT1]]
        T2Filter = dfT1[filterColumnT1] == filterColumnT2
        dfT2 = dfT1[T2Filter]
        Profit_Lost = dfT2.groupby(by = "Sub-Category").sum().sort_values(by="Lost-Profit", ascending = False).head(topInput)
        Profit_Lost = Profit_Lost.reset_index()
        barchart1 = sns.barplot(x="Lost-Profit", y= "Sub-Category", data=Profit_Lost)
        barchart1.set_title("Profit Lost to Discounts in "+str(filterColumnT2))
        #palette and hues
        sns.set(style="whitegrid", color_codes=True)
        pal = sns.color_palette("coolwarm", len(Profit_Lost))
        rank = Profit_Lost["Profit"].argsort().argsort()
        sns.barplot(x='Lost-Profit',y='Sub-Category',data=Profit_Lost, palette=np.array(pal[::-1])[rank])
        
        print(lines)
        plt.show()
        print("Red = Negative Profit \nBlue = Postive Profit \nColor Intensity = Relative Profitbility")
        print(lines)
        while not reset:
            resetInput = input("1) Show Raw Data \n2) Reset Filters \n3) Exit to Main Menu \nEnter a number to select:  ")
            if resetInput == "1":
                print(Profit_Lost.loc[:,["Sub-Category","Lost-Profit","Profit"]])
                continue
            elif resetInput == "2":
                reset = True
            elif resetInput == "3":
                loopin = False
                reset = True
            else:
                print("Sorry, that was an invalid menu option.")
#lostProfit()