#Variable to  house rows for the pyramid 
rows = 10

# Loop will run include a nested loop to help run through the rows that have been declared
for one in range(rows):
    #Nested loop will run through through items in that have already been looped through from the rows, but will then add and then multiply each item
    for two in range(one):
        time = two+1
        sum_ = time*one
        print(sum_, end=" ")# To create the pyramid using the end= label
    print("\n")

#Reference
# Capstone Project 1_Nested Loops Retrieved 22/08/2021 from C:\Users\user-pc\Dropbox\Naledi Motau-105175\Python for Data Science\Task 9\DS L1T09 - Capstone Project I_ Nested Loops .pdf
# Pyramid Patterns Retrieved 22/08/2021 from https://www.programiz.com/python-programming/examples/pyramid-patterns