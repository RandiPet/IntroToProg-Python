#-------------------------------------------------#
# Title: Assignment 06 TO DO List
#This program allows a user to store and edit a TODO list
# Dev:   Randi Peterson
# Date:  February 16, 2019
# ChangeLog: (Who, When, What)
#   RRoot, 11/02/2016, Created starting template
#   RPeterson, 2/10/2019, Added code to complete assignment 5
#   RPeterson   2/16/2019, Assignment 05 is modified to assignment 06
#https://www.tutorialspoint.com/python/python_dictionary.htm
#---------------------------1----------------------#

#Create a class for ToDoLst
class ToDoList:

    def ReadFile(self,objFileName):
        f = open(objFileName)
        strValues = ""
        dicRow = {}
        self.lstTable = [] #Creates a class variable

        # Step 1 - Load data from a file
        for line in f:  # Iterates over all rows in the file
            strValues = line.split(",")  # Comma separates the key and value
            dicRow = {strValues[0].strip(): strValues[1].strip()}  # Store in dictionary, will be overwritten each loop
            self.lstTable.append(dicRow)  # Attach dictionary to list
        f.close()

    #Step 2 - Display menu and take in user input
    def DisplayMenu(self):
        print("""
                Menu of Options
                1) Show current data
                2) Add a new item.
                3) Remove an existing item.
                4) Save Data to File
                5) Exit Program
                """)
        strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
        print()  # adding a new line
        return strChoice #Returns the choice so it later can be used by EvaluateInput

    #Step 3 - Display current list
    def DisplayList(self):
        for entries in self.lstTable:  # Go over full table
            for k in entries.keys():  # Go over all keys in dictionary (one per row)
                print(k + "," + entries[k])

    #Step 4 - Add item to list
    def AddItem(self):
        strNewItem = input("New item to add to ToDo List:")  # Get new item
        strNewPriority = input("New item priority:")  # Get priority for new item
        self.lstTable.append({strNewItem: strNewPriority})

    #Step 5 - Remove item from list
    def RemoveItem(self):
        strToRemove = input("Which task do you want removed?")
        tracker = []  # Tracker will note what indices contain the value to delete (in case of repeats)
        for index, entries in enumerate(self.lstTable):  # Goes through all values in self.lstTable and tracks indices
            if strToRemove in entries:
                tracker.append(index)  # Note the index at which the item to delete exists
        tracker.reverse()  # This is required so that it deletes from the end first. Otherwise, the list will slide up to fill the empty spot and mess up indexing.
        for i in tracker:
            self.lstTable.pop(i)  # remove using pop, which searches by index

    #Step 6 - Save list to .txt file
    def SaveList(self):
        file = open(objFileName, 'w')  # Reopen file to overwrite with new data
        for entries in self.lstTable:
            for k in entries.keys():  # Go over all keys in dictionary (one per row)
                file.write(k + "," + entries[k] + "\n")
        file.close()

    #Evaluate input/responses for menu
    def EvaluateInput(self,strChoice):
        # Step 3 -Show the current items in the table
        if (strChoice.strip() == '1'):
            self.DisplayList()
            return False #False prevents loop in MAIN from breaking
        # Step 4 - Add a new item to the list/Table
        elif(strChoice.strip() == '2'):
            self.AddItem()
            return False
        # Step 5 - Remove a new item to the list/Table
        elif(strChoice == '3'):
            self.RemoveItem()
            return False
        # Step 6 - Save tasks to the ToDo.txt file
        elif(strChoice == '4'):
            self.SaveList()
            return False
        #Exit program
        elif (strChoice == '5'):
            return True #Only case that breaks loop when returned

#MAIN
objFileName = "C:\_PythonClass\Assignment06\Todo.txt"
clsToDoLst = ToDoList()
2
#Call File Reading Function
clsToDoLst.ReadFile(objFileName)

while (True):
    strInput = clsToDoLst.DisplayMenu() #Displays menu, gets user input
    boolExit = clsToDoLst.EvaluateInput(strInput) #Uses user input to perform tasks
    #If the loop gets a true value (option 5) breaks loop
    if boolExit == True:
        break
