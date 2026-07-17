Favourite_pizzas = ['Margarita cheese', 'Cheese spinach and olive', 'Chicken pizza','Paneer pizza']
for Favourite_pizza in Favourite_pizzas:
    print(f"i love {Favourite_pizza} pizza ")
print("i really love pizza")

    
#Exercise 1: using Slice from index 0 to 3, but 3 is exclusive.

Pizzas = ['Margarita cheese', 'Cheese spinach and olive', 'Chicken pizza','Veg pizza','Paneer pizza']
print("The first three items in the lists are:", Pizzas[0:3] )


#Exercise 2: using slice from index 1 to 4 but 4 is exclusive.

Pizzas = ['Margarita cheese', 'Cheese spinach and olive', 'Chicken pizza','Veg pizza','Paneer pizza']
print("The middle three items in the lists are:", Pizzas[1:4])


#Exercise 3: using slice from index 2 to 5 but 5 is exclusive.

Pizzas = ['Margarita cheese', 'Cheese spinach and olive', 'Chicken pizza','Veg pizza','Paneer pizza']
print("The last three items in the lists are:", Pizzas[2:5])


#Exercise 4.1 from textbook:

Favourite_pizzas = ['Margarita cheese', 'Cheese spinach and olive', 'Chicken pizza','Paneer pizza']
Friend_pizzas = ['Margarita cheese', 'Cheese spinach and olive', 'Chicken pizza','Veg pizza']

print("My favourite pizzas are:")
print(Favourite_pizzas)

print("My friends favourite pizzas are:")
print(Friend_pizzas)





#Exercise same program with for loop.

Favourite_pizzas = ['Margarita cheese', 'Cheese spinach and olive', 'Chicken pizza','Paneer pizza']
print("My favourite pizzas are: ", end="")  # end= is a keyword argument in python.
for pizza in Favourite_pizzas:
    print(pizza, end=", ")

print("\n")  # Move to a new line. 
              # By writing print() the second line of output starts with a new line,
              # but with the print("\n") it gives the second output in new line and also gives one line gap between two lines.


Friend_pizzas = ['Margarita cheese', 'Cheese spinach and olive', 'Chicken pizza','Veg pizza']
print("My friends favourite pizzas are:", end="")    
for pizza in Friend_pizzas:
    print(pizza, end=", ")


#Exercise 
Animals = ['Lioness', 'Tigress', 'Cheetah']
for i in range (len(Animals)):
    if i == 0:
        print("A female Lion is called Lioness ")
    elif i == 1:
        print("A female Tiger is called Tigress")
    elif i == 2:
        print("Both female and male cheetah is called as Cheetah")

print("All these animals are wild animals")

#Exercise
for i in range (1, 21):
    print(i) 

#Exercise
# Excercise_1:this lists numbers from range 1 to 100000
million = list(range(1, 1000001))
print(million)


# Excercise_2:this lists numbers from range 1 to 100000 and it is gonna return minimum number, maximum number, sum number from the numbers in the list
million = list(range(1, 1000001))
print(min(million))
print(max(million))
print(sum(million))

#Exercise
odd_num = list(range(1, 21, 2))

for number in odd_num:
    print(number) 

##Exercise: 1
# ** is the symbol for cube in python 
for number in range (1, 11):
    print(number**3)


#Exercise: 2
#List comprehension
cube = [number**3 for number in range(1, 11)]
print(cube)

#Tuple.
#Exercise 1: Buffet fixed foods list without for loop. 
print("Without for loop")
Starters = ('Chicken lolipop', 'chicken kabab', 'chicken dry', 'fried chicken', 'dragon chicken')
print( "Resturants fixed starters are:", Starters)
    
print("\n")


#Exercise 2: Buffet fixed foods list with for loop.

print("With for loop")
Starters = ('Chicken lolipop', 'chicken kabab', 'chicken dry', 'fried chicken', 'dragon chicken')
print("These are the basic buffet foods:")
for starter in Starters:    
    print(starter)


# Excercise_1:this lists numbers from range 1 to 100000
million = list(range(1, 1000001))
print(million)


# Excercise_2:this lists numbers from range 1 to 100000 and it is gonna return minimum number, maximum number, sum number from the numbers in the list
million = list(range(1, 1000001))
print(min(million))
print(max(million))
print(sum(million))

#Exercise
odd_num = list(range(1, 21, 2))

for number in odd_num:
    print(number) 

#Exercise
#Making a list  of multiples of 5, 5 to 50.
for multiple in range(5, 50, 5):
    print(multiple)

#Making a list of multiples of 3, 3 to 30.
for number in range (3, 30, 3):
    print(number)



#Exercise
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
              

