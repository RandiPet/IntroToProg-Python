#-------------------------------------------------#
# Title: Assignment 07 Pickling and Exception Handling
#This program demonstrates how to do exception handling and pickling
# Dev:   Randi Peterson
# Date:  February 21, 2019
# ChangeLog: (Who, When, What)
#   RPeterson   2/21/2019, Creating script
#---------------------------1----------------------#

#Pickle is a module that must be imported
import pickle

#Create some lists of dummy data to play with
lstPeter = ["Peter","Piper","Picked","Pickled","Peppers"]
lstRhymes = ["tickle","fickle","sickle","trickle","nickel"]

#Print the original lists
print(lstPeter)
print(lstRhymes)

#Ask for user input
strInput = input("Pick your index, 0-4: ")

try:
    #Cast the string input to an int
    intInput = int(strInput)
    #Print the index selected
    print("Item " + str(intInput) + " is " + lstPeter[intInput])
    #Delete the index selected
    strRemovedItem = lstPeter.pop(intInput)

    #Print which item name was removed
    print(strRemovedItem + " was removed from the list")

#What to except when you're excepting
except:
    #Error is thrown if 1) string cannot be cast to int (i.e. it is a letter) 2) if the index is out of range (>4)
    print("That was not a valid index! Please follow directions.")

#STOP... it's Pickle Time

#Open file called PickleyPeppers.dat, wb will write to and create the file if it does not exist
objFile = open("PickleyPeppers.dat","wb")

#Dump lists to be pickled, close file
pickle.dump(lstPeter,objFile)
pickle.dump(lstRhymes,objFile)
objFile.close()

#Open up the pickled list. Read back the data (unpickled)
objFile = open("PickleyPeppers.dat","rb")
Peter = pickle.load(objFile)
Rhyme = pickle.load(objFile)

#Print the unpickled data
print("The file PickleyPeppers.dat contains: ")
print(Peter)
print(Rhyme)
