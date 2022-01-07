# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 13:06:09 2018

@author: cobuser

login emails
bob.moore@gmail.com     bob


"""

import sqlite3
conn = sqlite3.connect("OS_Employee.db")

def registration():
    with conn:
        cur = conn.cursor()
        try:
            #Automatically generates a 4 digit registerID based on the count of employees in the database
            cur.execute("SELECT COUNT(EmployeeID) FROM Employee")
            employeeCount = cur.fetchone()
            registerID = str(employeeCount[0] + 1).zfill(4)
        
            #Assures the registerID is UNIQUE, incrementing it by 1 untill it is.
            cur.execute("SELECT COUNT(EmployeeID) FROM Employee WHERE EmployeeID = ?", (registerID,))
            IdExistance = cur.fetchone()
            while IdExistance[0] == 1:
                registerID = int(registerID) + 1
                registerID = str(registerID).zfill(4)
                cur.execute("SELECT COUNT(EmployeeID) FROM Employee WHERE EmployeeID = ?", (registerID,))
                IdExistance = cur.fetchone()
                  
            print("="*10 + "[ User Registration ]" + "="*10)
            
            firstName = ''
            while not firstName:
                firstName = input("Please enter your first name: ")
                firstName = firstName.strip()
                firstName = firstName.title()
                
            lastName = ''
            while not lastName:
                 lastName = input("Please enter your last name: ")
                 lastName = lastName.strip()
                 lastName = lastName.title()
                 
            userEmail = ''
            while not userEmail:
                userEmail = input("Please enter your email: ")
                userEmail = userEmail.strip()
                userEmail = userEmail.lower()
            cur.execute("SELECT COUNT(Email) FROM Employee WHERE Email = ?", (userEmail,))
            emailExistance = cur.fetchone()
            while emailExistance[0] == 1:
                print("This email is already registered! Please enter a new email address.")
                userEmail = input("Please enter your email: ")
                userEmail = userEmail.strip()
                userEmail = userEmail.lower()
                cur.execute("SELECT COUNT(Email) FROM Employee WHERE Email = ?", (userEmail,))
                emailExistance = cur.fetchone()
            
                
                
            userPassword = input("Please enter your password: ")
            userPassword = userPassword.strip()
            while not userPassword:
                userPassword = input("Please enter your password: ")
                userPassword = userPassword.strip()
        
            cur.execute("INSERT INTO Employee VALUES (?, ?, ?, ?, ?)", (registerID, firstName, lastName, userEmail, userPassword))
            cur.execute("SELECT * FROM Employee WHERE EmployeeID = ?", (registerID,))
            results = cur.fetchone()
            
            lines = "="*40
            print("\n" + lines + "\n")
            print(results[1]+" "+ results[2] +" successfully registered!")
            print("\nEmployee ID: "+ results[0])
            print("Employee Email: "+ results[3])
            print("Passsword: "+ "*"*len(userPassword))
        except:
            print("Connection failed...")
            
def login():
    with conn:

        loginTest = False 
        while not loginTest:
            cur = conn.cursor()
            try:
                userEmail = input("Please enter your email: ")
                userEmail = userEmail.strip() 
                while not userEmail:
                    userEmail = input("Please enter your email: ")
                    userEmail = userEmail.strip() 
                    
                userPassword = input("Please enter your password: ")
                userPassword = userPassword.strip()
                while not userPassword:
                    userPassword = input("Please enter your password: ")
                    userPassword = userPassword.strip()
           
                cur.execute("SELECT COUNT (*) FROM Employee WHERE(Email = '" + userEmail.lower() +"' AND Password = '" + userPassword + "') ")
                results = cur.fetchone()
                if results[0]==1:
                    print("Login successful")
                    loginTest = True
                else:
                    print("Login unsuccessful. Please try logging in again.")
            except:
               print ("Connection failed")
