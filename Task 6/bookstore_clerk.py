####################################
# Creating the database that will be used to for the BookStore program

# Imports needed for the program
from os import truncate
import sqlite3


# Creating the Table/Database with the cursor object

db = sqlite3.connect('ebookstore_test_db')

books_cursor = db.cursor()

def create_table():
    books_cursor.execute('''
        CREATE TABLE books(
            id INTEGER,
            Title TEXT,
            Author TEXT,
            Qty INTEGER
        )
    ''')

    db.commit()
    #db.close()

# Inputting the data 
records =[
    (3001,"A Tale of Two Cities","Charles Dickens",30),
    (3002,"Harry Potter and the Philosopher's Stone","J.K Rowling",40),
    (3003,"The Lion, The Witch and the Wardrobe","C.S Lewis",25),
    (3004,"The Lord of the Rings","J.R.R Tolkien",37),
    (3005,"Alice in Wonderland","Lewis Caroll",12)    
]

# Function for the original data
def original_data():
    books_cursor.executemany('''
        INSERT OR IGNORE INTO books(id,Title,Author,Qty) VALUES(?,?,?,?)
    ''',records)
    db.commit()
    #db.close()
    
# Function to add the new record        
def add_data():
    # Input data that will add new records
    insert_id = input("Please enter a new ID for newly added book: ")
    insert_title = input("Please enter title of the new book: ")
    insert_author = input("Please enter the author of the new book: ")
    insert_qty = int(input("please enter the Quantity of books you currently stocked: "))

    books_cursor.execute('''
        INSERT OR IGNORE INTO books(id,Title,Author,Qty) VALUES(?,?,?,?)
    ''',(insert_id,insert_title,insert_author,insert_qty))
    db.commit()
    print('New record has been inserted')


#===================================================================================    
# Function to display the entire records within the table
def display_data():
    sum_display = 0
    books_cursor.execute('''
        SELECT * FROM books
    ''')

    books_display = books_cursor.fetchall()
    
    # Loop to print data in a readable format
    print("Bookstore Data....\n")
    for row in books_display:
        print("id: ", row[0])
        print("Title: ", row[1])
        print("Author: ", row[2])
        print("Qty: ", row[3])
        print('\n')
        sum_display += 1
    
    print("***Table has been  displayed, there are currently {} records in the table****\n".format(sum_display))
    

# Function to display a record within the table
def display_record():
    display_record = input("Please enter the Name of the book you'd like to display: ")
    
    # Query to find a record based on the Title of the book
    books_cursor.execute('''
        SELECT *
        FROM books
        WHERE Title = ?
    ''',(display_record,))

    # To display the record
    record_display = books_cursor.fetchone()
    print("Bookstore Record Data....\n")
    print("id: ", record_display[0])
    print("Title: ", record_display[1])
    print("Author: ", record_display[2])
    print("Qty: ", record_display[3])
    print("\n")
    print("***Record has been  displayed****\n")
    
#=================================================================================
# Function to update an entire record or just the selected field within the record.
def update_data():

    #Input variable that will select whether we update an entire row or just the selected field
    update_input = input("Would you like to update the entire row or just a single field? please answer row or field: ")

    # If Row is selected, we update the row
    if update_input == "row":
        print("Please update all the fields that need to be changed")
        
        # Inputs that will be used to update the fields
        update_title = input("New Title for record: ")
        update_author = input("New Author of the book: ")
        update_qty = int(input("New number of stock: "))
        current_title = input("Name of the title you would like to change: ")
        
        #SQL Query to update
        books_cursor.execute('''
            UPDATE books
            SET Title = ?, Author = ?, Qty = ?
            WHERE Title =?
        ''',(update_title,update_author,update_qty,current_title))
        db.commit()
        print("\n{} record has been updated".format(current_title))

    #To update the selected fields within the row
    elif update_input == "field":

        # Updating the Title
        update_input_type = input("Please select the Column you'd like to update between Title, Author or Qty: ")
        if update_input_type == "Title":
            print("Please update the Title of the book")
            update_title = input("New Title for record: ")
            current_title = input("Name of the title you would like to change: ")
            books_cursor.execute('''
                UPDATE books
                SET Title = ?
                WHERE Title =?
            ''',(update_title,current_title))
            db.commit()
            print("\n{} title has been updated to {}".format(current_title,update_title))

        # Updating the Author
        elif update_input_type == "Author":
            print("Please update the Author of the Title you'd like to change.")
            update_author = input("New Author of the book: ")
            current_title = input("Author of the title you would like to change: ")
            books_cursor.execute('''
                UPDATE books
                SET Author = ?
                WHERE Title =?
            ''',(update_author,current_title))
            db.commit()
            print("\n{} Author has been updated".format(current_title))

        # Updating the Qty
        elif update_input_type == "Qty":
            print("Please update the Quantity of books of selected Title")
            update_qty = input("New number of stock: ")
            current_title = input("Qty of the title you would like to change: ")
            books_cursor.execute('''
                UPDATE books
                SET Qty = ?
                WHERE Title =?
            ''',(update_qty,current_title))
            db.commit()
            print("\n{} Qty has been updated".format(current_title))
#==============================================================================
# Function to deleta a record within the table
def delete_data():

    # input variable to select the book we would like to delete
    delete_record = input("Please delete the record of the Title you selected: ")
    
    # SQL Query
    books_cursor.execute('''
        DELETE FROM books
        WHERE Title = ?
    ''',(delete_record,))
    db.commit()
    print("\n{} has been deleted...\n".format(delete_record))

# Creating the menu for the bookstore_clerk program

menu = "\n1.Enter book \n2.Update book \n3.Delete book \n4.Search books \n0.Exit"




def quit_program():
    
    if book_input == "0":
        quit()



while True:
    # Title
    print("Welcome to the Book Store \nPlease select the items from the menu below ")
    
    # Menu
    print(menu)

    # Input that will be used to select the menu
    book_input = input("\nWhat would you like to do, please select a number as displayed from the menu: ")

    # If statements that will run the declared functions of our SQL statements
    if book_input == '1':
        
        add_data()
        
    elif book_input == '2':
        
        update_data()
        
    elif book_input == '3':
        
        delete_data()
        
    elif book_input == '4':
        
        search = input("Would you like to search the entire table or just a specific row, please select table or row: ")
        
        if search == "table":
            display_data()
            
            #menu_app()
            

        elif search == "row":
            display_record()
            
    
    elif book_input == "0":
        print("Thank you for using the book store application.")
        quit_program()
    


#################################################################
# Database and Table have already been created, please test the Menu items.

# References
# SQLite retrieved 14/10/2021 from C:\Users\user-pc\Dropbox\Naledi Motau-105175\Data Analytics and Exploration\Task 5\DS L2T05 - SQLite.pdf
# Working with SQL retrieved 14/10/2021 from file:///C:/Users/user-pc/Dropbox/Naledi%20Motau-105175/Data%20Analytics%20and%20Exploration/Task%204/DS%20L2T04%20-%20Working%20with%20SQL.pdf
# Python exit command retrieved 14/10/2021 from https://pythonguides.com/python-exit-command/
# Inserting multiple rows to table retrieved 14/10/2021 from https://pythonexamples.org/python-sqlite3-insert-multiple-rows-to-table/
# Insert values to a table from user input retrieved 14/10/2021 from https://www.w3resource.com/python-exercises/sqlite/python-sqlite-exercise-7.php
# Select from table retrieved 14/10/2021 from https://pynative.com/python-sqlite-select-from-table/



# Discord disagreement