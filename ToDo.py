#-------------------------------------------------#
# Title: Assignment 05 TO DO List
#This program allows a user to store and edit a TODO list
# Dev:   Randi Peterson
# Date:  February 10, 2019
# ChangeLog: (Who, When, What)
#   RRoot, 11/02/2016, Created starting template
#  RPeterson, 2/10/2019, Added code to complete assignment 5
#https://www.tutorialspoint.com/python/python_dictionary.htm
#---------------------------1----------------------#

objFileName = "C:\_PythonClass\Assignment05\Todo.txt"
f = open(objFileName)
strData = ""
dicRow = {}
lstTable = []

# Step 1 - Load data from a file
    # When the program starts, load each "row" of data 
    # in "ToDo.txt" into a python Dictionary.
    # Add the each dictionary "row" to a python list "table"

for line in f: #Iterates over all rows in the file
    strValues = line.split(",") #Comma separates the key and value
    dicRow = {strValues[0].strip():strValues[1].strip()} #Store in dictionary, will be overwritten each loop
    lstTable.append(dicRow) #Attach dictionary to list

f.close()

# Step 2 - Display a menu of choices to the user
while(True):
    print ("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()#adding a new line

    # Step 3 -Show the current items in the table
    if (strChoice.strip() == '1'):
        for entries in lstTable: #Go over full table
            for k in entries.keys(): #Go over all keys in dictionary (one per row)
                print(k + "," + entries[k])

    # Step 4 - Add a new item to the list/Table
    elif(strChoice.strip() == '2'):
        strNewItem = input("New item to add to ToDo List:") #Get new item
        strNewPriority = input("New item priority:") #Get priority for new item
        lstTable.append({strNewItem: strNewPriority})

    # Step 5 - Remove a new item to the list/Table
    elif(strChoice == '3'):
        strToRemove = input("Which task do you want removed?")
        tracker = [] #Tracker will note what indices contain the value to delete (in case of repeats)
        for index, entries in enumerate(lstTable): #Goes through all values in lstTable and tracks indices
            if strToRemove in entries:
                tracker.append(index) #Note the index at which the item to delete exists
        tracker.reverse() #This is required so that it deletes from the end first. Otherwise, the list will slide up to fill the empty spot and mess up indexing.
        for i in tracker:
            lstTable.pop(i) #remove using pop, which searches by index

    # Step 6 - Save tasks to the ToDo.txt file
    elif(strChoice == '4'):
        file = open(objFileName,'w') #Reopen file to overwrite with new data
        for entries in lstTable:
            for k in entries.keys(): #Go over all keys in dictionary (one per row)
                file.write(k + "," + entries[k]+"\n")
        file.close()

    #Exit program
    elif (strChoice == '5'):
        break #and Exit the program
