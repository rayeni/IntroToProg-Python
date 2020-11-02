# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RAyeni,10.30.2020,Added code to complete assignment 5
# ------------------------------------------------------------------------ #


# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"  # Variable to reference file name.
lstRow = []  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # A Capture the user option selection
taskNum = ""  # A variable to reference row to remove
task = ""  # A variable to reference task to do
priority = ""  # A variable to reference task's priority
confirmRm = ""  # User confirmation of removal of task


# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

# MODIFICATION - by RAyeni
try:
    objFile = open(strFile, "r")
    for row in objFile:
        lstRow = row.split(",")
        dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
        lstTable.append(dicRow)
    objFile.close()
except:
    print("")



# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
        To-Do List
        
    Menu of Options
    1) Show current data.
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File.
    5) Exit Program.
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # MODIFICATION - by RAyeni
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        if len(lstTable) == 0:  # Action to perform if table is empty
            print("There are no data to display.")
        else:  # Action to do if table is not empty
            j = 0  # variable used to number rows
            print("Task No. | Task \t| Priority\n")
            for row in lstTable:
                print(f'{j} | {row["Task"]} \t| {row["Priority"]}')
                j += 1
        continue

    # MODIFICATION - by RAyeni
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        task = input("To-Do Item: ")  # User enters task
        priority = input("To-Do Item Priority (High, Medium, Low): ")
        dicRow = {"Task": task, "Priority": priority}  # Put entries in dict.
        lstTable.append(dicRow)  # Append dict to table/nested list
        continue

    # MODIFICATION - by RAyeni
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        i = 0  # local variable to act as counter to number rows
        print("Task No. | Task \t| Priority\n")  # Data header
        for row in lstTable:  # loop through list of dictionaries
            print(f'{i} | {row["Task"]} \t| {row["Priority"]}')
            i += 1
        print()  # print new line
        # Capture row number to delete
        taskNum = int(input("Select task (0, 1, 2, ..) to remove: "))
        # Confirm deletion of selected row
        confirmRm = input(f'Remove Task No. {taskNum}? Enter y or n: ')
        if confirmRm.lower() == "y":  # Condition to remove row
            lstTable.pop(taskNum)  # Remove row
            print(f'\nTask {taskNum} has been removed.')
        elif confirmRm.lower() == "n":  # Condition to not remove row
            print(f'\nTask {taskNum} has NOT been removed.')
        else:
            print("Incorrect choice. No action taken. ")
        continue

    # MODIFICATION - by RAyeni
    # Step 6 - Save data to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(strFile, "w")
        for row in lstTable:
            objFile.write(row.get("Task") + "," + row.get("Priority") + "\n")
        objFile.close()
        print("Data saved to", strFile)
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        break  # Exit while loop

# MODIFICATION - by RAyeni
# Exit script
input("\nPress the Enter key to exit.")
