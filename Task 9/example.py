
#************* HELP *****************
#REMEMBER THAT IF YOU NEED SUPPORT ON ANY ASPECT OF YOUR COURSE SIMPLY LOG IN TO www.hyperiondev.com/support TO:
#START A CHAT WITH YOUR MENTOR OR SCHEDULE A CALL.
#*************************************


# PLEASE ENSURE YOU OPEN THIS FILE IN IDLE otherwise you will not be able to read it.

# *** NOTE ON COMMENTS ***
# This is a comment in Python.
# Comments can be placed anywhere in Python code and the computer ignores them - they are intended to be read by humans.
# Any line with a # in front of it is a comment.
# Please read all the comments in this example file and all others.


# ============= Nested Loops ==================
# Now that you have experience using loops we are going to consolidate that knowledge by introducing you to Nested Loops.
# A nested loop simply put is a loop within a loop.
# Each time the outer loop is executed, the inner loop is executed right from the start.
# That is, all the iterations of the inner loop is executed with each iteration of the outer loop.

# ************ Example 1 ************
# The syntax for a nested for loop in another for loop is as follows:
# sequence =[]
# for iterating_var in sequence:
#   for iterating_var in sequence:
#      statements(s)
#   statements(s)

# ************ Example 2 ************
# The syntax for a nested while loop in another while loop is as follows:
# while condition:
#    while condition:
#       statement(s)
#   statement(s)

# ************ Example 3 ************
# You can put any type of loop inside of any other type of loop.
# For example, a for loop can be inside a while loop or vice versa.

# sequence =[]
# for iterating_var in sequence:
#    while condition:
#       statement(s)
#   statements(s)

# ************ Example 4 ************
# This example prints out the first 5 multiples of numbers 1 to 5

print ("Example 4: ")

for x in range(1, 6):
    for y in range(1, 6):
        print ('%d x %d = %d' % (x, y, x*y))
    print ("")

# Run this program to see the output

# ============= Nested if Statements ==================
# You can also nest if statements either within another if statement or within a loop

# ************ Example 5 ************
# Nested if statements
print ("Example 5: ")
name = "B"
if name == "A":
        if name =="B":
                print ("It isn't possible for this code to execute, how can the variable name be two things at once?")
else:
        print ("Your name isn't A but I can't automatically assume from that that it is B.")

# Think about this one logically! Note the indentation carefully. You have an if within an if and then an else.



# ****************** END OF EXAMPLE CODE ********************* #


# == Make sure you have read and understood all of the code in this Python file.
# == Please complete the compulsory task below to proceed to the next task ===
# == Ensure you complete your work in this folder so that one of our tutors can easily locate and mark it ===
