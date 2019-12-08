# Problem 1

Sample_str = "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"

New_str_1 = """Twinkle, twinkle, little star,
    How I wonder what you are!
        Up above the world so high,
        Like a diamond in the sky.
Twinkle, twinkle, little star,
    How I wonder what you are
"""

New_str_2 = "Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\t How I wonder what you are"

print(New_str_1)
print(New_str_2)

# Problem 2

import sys

print(sys.version)
print(sys.version_info)

# Problem 3

import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

# Problem 4

r = float(input("Pls enter the radius: "))
print("The radius you inputted was _" + str(r) + "_ units... The area of the circle with your radius is _" + str(3.1415926535 * r**2) + "_ square units")

# Problem 5

f_name = str(input("Pls enter your first name: "))
l_name = str(input("Pls enter your last name: "))

print("Your name reversed is: " + l_name + " " + f_name)
print("Your official - sounding name is: " + l_name + ", " + f_name)

#! Problem 6

#! Problem 7

# Problem 8

color_list = ["Red","Green","White" ,"Black"]

print(color_list[0], color_list[-1])

#! Problem 9

#! Problem 10

#! Problem 11
 
# Problem 12

import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))

# Problem 13

print("""
a string that you "don't" have to escape
This
is a  ....... multi-line
heredoc string --------> example
""")

#! Problem 14

# Problem 15

radius = 6
print("The volume of a sphere with a radius of 6 is 904.78 ** 3 units")

# Problem 16

input_num = int(input("Enter your number: "))

if input_num - 17 == 0 or input_num - 17 < 0:
    print(abs(input_num) * 2)

# Problem 17

