#Exercise 01:
#Rental cars.

rental_car = input("Please enter the car you are looking for to rent.")
print(f"Please wait a moment let me check the {rental_car} you are looking for. ")


#Exercise 02:
#Restaurant seating

seats = int(input("Hello, a table for how many people?")) 
if seats > 8 :
    print("All tables are occupied, please wait for a while.")
else:
    print("Your table is ready.")

    #Exercise 03:
#Multiples of ten

num = int(input("Give me a number:"))
if num % 10:
    print(f"{num} is multiple by 10.")
else:
    print(f"{num} is not multiple by 10.")



#Exercise 04:
#pizza toppings

prompt = "\n Enter pizza topping of your choice: " #prompts are variables that holds the string values the details to the user.
prompt += "\n Enter 'quit' when you are done."

while True:  # while true is a while loop which is always true so we use while true when we want the while loop to run infinitely till something like break or flag stops the loop.
    pizza_topping = input(prompt) #pizza topping is the variable that holds the value of the prompt.
    if pizza_topping == 'quit': #when the user types quit then the loop stops with the help of break.
        break  #break stops the loop.

print("Thank you, we will add these toppings on your pizza.")


#Exercise 05:
#Theatre tickets

prompt = ("\n[Please type stop when you are done with the tickets.]")
prompt += ("\nPlease enter your age: ")


while True:  #we used while true because we want the loop to run until we stop if externally with break .
        age = input(prompt) #here we are assigning the prompt to the variable name age.
        if age == 'stop': #we are putting a condition that says if the age becomes stop then the loop should stop. 
             break  #this stops the loop.
        age = int(age) # here we are turning the user input to integer. 

        if age <= 3: 
            print("Theatre fare is free for you.")
        elif age > 3 and age < 12:
            print("Your fare is 10$.")
        elif age > 12 :
            print("Your fare is 15$.")   
#Mistakes i made in this you are comapring age in if condition which is an integer and to 
#,use stop you have to put the break before you convert the age into integer.            


#Exercise 06:
#Three exits 

#Version 01, using the conditional test in while statement to stop the loop :

prompt = "\n Enter pizza topping of your choice: " 
prompt += "\n Enter 'quit' when you are done."

topping = input(prompt)

while topping != 'quit': # here i have used a conditional test in the while loop this stops the while loop when the variable topping becomes quit.
    topping = input(prompt)

print("thank you for your order.")

#Version 02, using an active variable to control how long the loop runs.

prompt = ("[Please type 'quit' when you are done.]")
prompt += ("\nPlease enter your choice of topping:")

topping = input(prompt)

while True: # here we are using a active variable in while loop.
    topping = input(prompt)
    if topping == 'quit':
        break

print("Thank you for your order.")


#Exercise 07:
#infinity loop 

topping = input("Please enter your choice of topping:")

while True:
    print ("thank you.")
    break #here i have added break because the vsc was making all the other programs after this grey because this is an infinite loop. 


#Exercise 08:
#Deli

sandwich_orders = ['chicken sandwich', 'paneer sandwich', 'soyachunk sandwich', 'chilli and cheese sandwich', 'egg sandwich']
finished_sandwich = []

while sandwich_orders:  # i a, looping the sandwich_orders 
    current_sandwich = sandwich_orders.pop() # when the python sees current_sandwich it creates new variable current_sandwich
    print(f"here is your {current_sandwich}") # and all the values we have poped from the sandwich_orders will be saved inside current_sandwich

    finished_sandwich.append(current_sandwich) #here we are adding the values in the current_sandwich to the variable finished_sandwich. 
   
print("\nthe following sandwich were made :") 

for sandwich in finished_sandwich: # here for loop is to print all the value which is in the finished sandwich.
    print(sandwich) # here we have used just sandwich rather than finished_sandwich,
                    # because finished sandwich whill print all the value 5 times but just sandwich will print the each sandwich names just one time. 
#in this important thing is to remove a value from one list and append it to another list.   


#Exercise 09:
#No pastrami

sandwich_orders = ['chicken sandwich', 'pastrami' ,'paneer sandwich', 'soyachunk sandwich', 'pastrami' ,'chilli and cheese sandwich', 'egg sandwich', 'pastrami',]
finished_sandwich = []

print("the deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:  #here i have added another while loop to remove all the pastrami from the list.
        sandwich_orders.remove('pastrami')  

while sandwich_orders:  # i a, looping the sandwich_orders 
    current_sandwich = sandwich_orders.pop() # when the python sees current_sandwich it creates new variable current_sandwich
    
    
    print(f"here is your {current_sandwich}") # and all the values we have poped from the sandwich_orders will be saved inside current_sandwich

    finished_sandwich.append(current_sandwich) #here we are adding the values in the current_sandwich to the variable finished_sandwich. 
   
print("\nthe following sandwich were made :") 

for sandwich in finished_sandwich: # here for loop is to print all the value which is in the finished sandwich.
     print(sandwich) # here we have used just sandwich rather than finished_sandwich,
                         # because finished sandwich whill print all the value 5 times but just sandwich will print the each sandwich names just one time. 
                          #in this important thing is to remove a value from one list and append it to another list.   

#Exercise 10:
#Dream vacation


vacation_poll = {}

while True:
    name = input("Please enter your name : ")
    vacation = input(f"{name}, if you could visit one place in the world, where would you go? :")
    response = input("would you like to continue?")
    
    vacation_poll[name] = vacation

    if response == 'no':
        break

print("These are the people who took the poll:")

for name, vacation, in vacation_poll.items():
    print(f"{name}, would love to visit {vacation}.")

#A dictionary cannot have duplicate keys. 
#keys with the same name cannot exist.

#Exercise
filename = "python_notes.txt"
print(filename.removesuffix(".txt"))
