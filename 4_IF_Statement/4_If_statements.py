#Conditional test:

#Exercise 1:  
car = 'subaru'  #Here car is a variable with a value 'subaru'
print("Is car == 'subaru'?")   #in this exercise we are doing conditional tests on two statements one is false and another is true. 
print(car == 'subaru')
print("\nIs car == 'audi'?")
print(car == 'audi')


#Exercise 2:   in this both values are false.
Hair_colour = 'Brown'
print("is hair colour == 'black'?")
print(Hair_colour == 'black')
print("\n is hair colour == 'white'?")
print(Hair_colour == 'white')
print("Hair colour is brown")


#Exercise 3:     in this both values are true.
Dessert = 'Cheese cake'
print("is Dessert == 'Cheese cake'?")
print(Dessert == 'Cheese cake')
print("\n is Dessert != 'Chocolate cake'?")
print(Dessert != 'chocolate cake')
print("Cheese cake is a dessert.")


#Exercise 4: in this first value is true and the second value is false.
Weather = 'Raining'
print("is Weather == Raining?")
print(Weather == 'Raining')  ## == is the conditional test.
print("\n is Weather == Sunny?")
print(Weather == 'Sunny')


#Exercise 5: in this  first value is false and the second value is true.
Name = 'Rakshitha'
print("is the Name Raksha?")
print(Name == 'Raksha')  # == is a conditional test.
print("is the Name Rakshitha?")
print(Name == 'Rakshitha')
print(f"{Name}, is a correct Name.")  # here i have used f string to use variable inside a string statement. 


#Alien Game:
#this is to exercise if statements.

#Exercise 1:
#This is the version were the if statement fails.
#Because the if statement fails here there is no output. 
alien_color = 'Red'
print(f"Your alien color is:{alien_color}") # i have used f string.
if alien_color == 'Green':
    print("You get 5 full points.")


#This is the version were the if statement passes.
alien_color = 'Green'
print(f"Your alien color is:{alien_color}")
if alien_color == 'Green':
    print("Congragulations you get five points.")


    
#Exercise 2:
#in this the if block runs because it is true.
alien_color = 'Green'
print(f"Alien color:{alien_color}")
if alien_color == 'Green':
    print("You get five points for shooting down an alien.") #running in the if block.
else:
    print("No points")


#in this the else block runs because it is true.
alien_color = 'Red' 
print(f"Alien color:{alien_color}")
if alien_color == 'Green':
    print("You get five points")
else:
    print("You earned 10 points")  # running in the else block.


#IF-ELIF-ELSE.
#Exercise 3:

#Version 01:
alien_color = 'Green'
print(f"Alien color:{alien_color}")
if alien_color == 'Green':     #Here if statement runs.
    print("You earned 5 points")
elif alien_color == 'Red':
    print("You earned 10 points")
else:
    print("You earned 15 points")

#Version 02:
alien_color = 'Red'
print(f"Alien color:{alien_color}")
if alien_color == 'Green':
    print("You earned 5 points")
elif alien_color == 'Red':      #Here elif statement runs.
    print("You earned 10 points")
else:
    print("You earned 15 points")

#Version 03:
alien_color = 'Yellow'
print(f"Alien color:{alien_color}")
if alien_color == 'Green':
    print("You earned 5 points")
elif alien_color == 'Red':
    print("You earned 10 points")
else:                           #Here else statement runs.
    print("You earned 15 points")

#Stages of life:

#Version 01:
age = 1
if age <= 2:   #here this if condition runs.
    print("A baby")
elif age >= 2 and age <=4 :
    print("A toddler")
elif age >= 4 and age <= 13 :
    print("A kid")
elif age >= 13 and age <= 20 :
    print("A teenager")   
elif age >=20 and age <= 65 : 
    print("A adult")
else:
    print("A elder")


#Version 02:
age = 3
if age <= 2:   
    print("A baby")
elif age >= 2 and age <=4 :  #here this elif condition runs.
    print("A toddler")
elif age >= 4 and age <= 13 :
    print("A kid")
elif age >= 13 and age <= 20 :
    print("A teenager")   
elif age >=20 and age <= 65 : 
    print("A adult")
else:
    print("A elder")


#Version 03:
age = 11
if age <= 2:
    print("A baby")
elif age >= 2 and age <=4 :
    print("A toddler")
elif age >= 4 and age <= 13 :  #here this elif condition runs.
    print("A kid")
elif age >= 13 and age <= 20 :
    print("A teenager")   
elif age >=20 and age <= 65 : 
    print("A adult")
else:
    print("A elder")


#Version 04:
age = 19
if age <= 2:
    print("A baby")
elif age >= 2 and age <=4 :
    print("A toddler")
elif age >= 4 and age <= 13 :
    print("A kid")
elif age >= 13 and age <= 20 :  #here this elif condition runs.
    print("A teenager")   
elif age >=20 and age <= 65 : 
    print("A adult")
else:
    print("A elder")


#Version 05:
age = 59
if age <= 2:
    print("A baby")
elif age >= 2 and age <=4 :
    print("A toddler")
elif age >= 4 and age <= 13 :
    print("A kid")
elif age >= 13 and age <= 20 :
    print("A teenager")   
elif age >=20 and age <= 65 :   #here this elif condition runs.
    print("A adult")
else:
    print("A elder")


#Version 06:
age = 77   
if age <= 2:
    print("A baby")
elif age >= 2 and age <=4 :
    print("A toddler")
elif age >= 4 and age <= 13 :
    print("A kid")
elif age >= 13 and age <= 20 :
    print("A teenager")   
elif age >=20 and age <= 65 : 
    print("A adult")
else:                   #here this else condition runs.
    print("A elder")



#Favourite fruits
#in this program we are gonna use multiple if statements for one list

#if statement 01:
Favourite_fruits = ['Watermelon', 'Mango', 'Pear']
if 'Mango' in Favourite_fruits:
    print("You love mangos")


#if statement 02:
Favourite_fruits = ['Watermelon', 'Mango', 'Pear']
if 'Apples' in Favourite_fruits:
    print("You love apples")



#if statement 03:
Favourite_fruits = ['Watermelon', 'Mango', 'Pear']
if 'Watermelon' in Favourite_fruits:
    print("You love watermelons")


#if statement 04:
Favourite_fruits = ['Watermelon', 'Mango', 'Pear']
if 'Pear' in Favourite_fruits:
    print("You love Pears")


#if statement 05:
Favourite_fruits = ['Watermelon', 'Mango', 'Pear']
if 'Orange' in Favourite_fruits:
    print("You love Oranges")


#Exercise 1:
#Looping through usernames.

Username = ['Admin','Raksha','Pooja','Yashu','Siddhu']

for usernames in Username :
    if usernames == 'Admin': #Here i did a minor mistake i rather than writing usernames i wrote Username which didnt give me the output i needed.
         print("Hello Admin welcome back, latest NDA report will open in 2 minutes.")     
    else:
         print(f"Hello {usernames} welcome back")  #Give space either side of flower braces for the output to come clean.



#Exercise 2:
#No users
#if test

#Version 01: with the comparision operator.(==)
Username = []
print(f"Usernames:{Username}")
if Username == []:
    print("We have to find some users.")


#Version 02: with the membership operator (in , not in)
Username = []
if not Username:
    print("Username list is empty.")



#Exercise 3:
#Checking usernames
Current_users = ['Raksha','Pooja','Yashu','Siddhu','Dhanveer']
New_users = ['Raksha','Nagu','Anu','Giri','Pooja']
for New_user in New_users:
    if New_user in Current_users:  # the mistake i did is i used comparision operator but when we are comparing between lists we should always use membership operators.
        print("You need a new user name.")
    else:
        print("this user name is available")



#Ordinal numbers:

#Version 01 :
#With the membership operator(in).
Ordinal_num = ['1','2','3','4','5','6','7','8','9']
for Ordinal_nums in Ordinal_num:
    if '1' in Ordinal_nums:
        print(f"{Ordinal_nums}st")
    elif '2' in Ordinal_nums:
        print(f"{Ordinal_nums}nd")
    elif '3' in Ordinal_nums:
        print(f"{Ordinal_nums}rd")
    else:
        print(f"{Ordinal_nums}th")



print("\n")


#version 02 :
#With the comparision operator(==).
Ordinal_num = ['1','2','3','4','5','6','7','8','9']
for Ordinal_nums in Ordinal_num:
    if '1' == Ordinal_nums:
        print(f"{Ordinal_nums}st")
    elif '2' == Ordinal_nums:
        print(f"{Ordinal_nums}nd")
    elif '3' == Ordinal_nums:
        print(f"{Ordinal_nums}rd")
    else:
        print(f"{Ordinal_nums}th")
              

#Mistakes i did :
#in the if i was writting 1 but i should always check the value in the list exactly how i have writtten it in the list.
#so i changed 1 to '1' then my if condition started running.
#till then my if condition was not running because 1 was not in the list and i had not giving what should the list do if there that value doesnt exist.
                      