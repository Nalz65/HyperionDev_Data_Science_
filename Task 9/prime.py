#Declaring the factor and the input for the user
num_factor = 2 # The variable determines if there is only two numbers that can be make up the prime number

user_num = int(input("Please enter a number: "))

# Running an if statemtent for any number that is bigger than 1 to determine the prime number 
if user_num > 1:

    count = user_num -1 # the count will subtract the number the user entered to determine if it is a prime number

    while count > 1: # As long as the count is bigger than 1  
        if (user_num % count) == 0: # it will check the remainder if it is equal to zero, if so the num_factor will be added by one which will specify if there's more than one factor
            num_factor += 1
            break
        #The next line decrease the count of the inputted number
        count -= 1
else:
    print("the number is less than one")
 
# To check if num_factor is still equal to 2 once the above condition has been run. Will determine if entered number is a prime number
if num_factor == 2:
    print(str(user_num) + " Is a prime number")
else:
    print(str(user_num) + " Is not a prime number.")

# Reference
# Capstone Project 1_Nested Loops Retrieved 22/08/2021 from C:\Users\user-pc\Dropbox\Naledi Motau-105175\Python for Data Science\Task 9\DS L1T09 - Capstone Project I_ Nested Loops .pdf
# Prime Number Retrieved 22/08/2021 from https://www.programiz.com/python-programming/examples/prime-number
# How to find Prime Numbers Retrieved 22/08/2021 from https://www.vedantu.com/maths/how-to-find-prime-numbers