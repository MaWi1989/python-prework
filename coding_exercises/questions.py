#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.
#    def hello_name(user_name):

def hello_name(user_name):
    """"Send a simple greeting to each user."""
    print("hello_" + user_name.upper() + "!")
  
hello_name('username')

print("\n")
#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
#    def first_odds():

def first_odds():
    """Print all odd numbers from 1 to 100."""
    for number in range(1,101):
        if number % 2 == 0:
            continue
        else:
            print(number)

first_odds()

print("\n")
#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
#    def max_num_in_list(a_list):

def max_num_in_list(a_list):
    """Return the maximum number of a given list."""
    print(max(a_list))

a_list = [51, 4, 986, 264, 289]

max_num_in_list(a_list)


print("\n")
#Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, 
# but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).
#    def is_leap_year(a_year):

def is_leap_year(a_year):
    """Figure out if a given year is a leap year."""
    year = int(a_year)
    if year % 400 == 0:
        if year % 4 == 0 and year % 100 == 0:
            return True
    elif year % 400 != 0:
        if year % 4 == 0 and year % 100 != 0: 
            return True
    else:
        return False

leap_year = bool(is_leap_year(2020))
print(leap_year)


print("\n")
#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.
#    def is_consecutive(a_list):

def is_consecutive(a_list):
    """Check if all numbers in a given list are consecutive."""
    
    sorted_list = sorted(a_list)
    range_list = list(range(min(a_list), max(a_list)+1))

    if sorted_list == range_list:
        return True 
    else:
        return False
    
a_list = [5,6,7,8,10]
    
consecutive = bool(is_consecutive(a_list))
print(consecutive) 
    




 
