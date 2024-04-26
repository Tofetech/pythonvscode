
#Write a program that accepts user input as float, then convert to integer,
#using Modulo operator, 
#declare whether it is odd or even number inputted by the user.

float = int(float(input("Write a float number:")))

if float % 2 == 0:
    print("it is an even number")

else:
    print("it is odd")
