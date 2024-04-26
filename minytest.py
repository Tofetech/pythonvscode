 #1) #what would be the result of printing (x or y)?
x = 0
y = 5


#2) 
x = 3%2
y = x + 1
print(y)
#2 ANZ

#3) Ask user to input their year of birth, then calculate their current age.


birth = int(input("What is your year of birth",value=1995))
currentyear = int(input("What is the current year",value=2023))

age = currentyear - birth

print(age)

#4) Ask user to input a number, then determine whether the number is an odd or even number.
interger = int(input("Enter an integer number"))

if interger % 2  ==  0:
    print("It is even")

else:
    print("It is odd")
