#Exercise 01
#Restaurant:
class Restaurant: # i got invalid syntax here because i had not given colon after creating class.
    """Creating a class named Restaurant."""

    def __init__(self, restaurant_name, cuisine_type): #i got an invalid syntax here because i had not given space between def and __init__.
        """Initialize the restaurant's name and cuisine type."""
       
        self.restaurant_name = restaurant_name    # Store the values as instance attributes.We assign the value of the parameter restaurant_name to self.restaurant_name.-
        self.cuisine_type = cuisine_type             #-This creates an instance attribute, which is stored in the object.-
                                                      #-Every object created from the class gets its own restaurant_name and cuisine_type attributes.
    def describe_restaurant(self):  #self is a reference to the current object (instance), allowing the method to access that object's attributes and other methods.
        """Display the restaurant's name and cuisine type."""
       
        print(f"Restaurant name is {self.restaurant_name}")
        print(f"Cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        """Display a message indicating that the restaurant is open."""
       
        print(f"{self.restaurant_name} is OPEN.")

restaurant = Restaurant('Meghana','Non-veg')
# Create an instance of Restaurant.

print(f"Restaurant {restaurant.restaurant_name}")
print(f"The cuisine is {restaurant.cuisine_type}")

# Call both methods.
restaurant.describe_restaurant()
restaurant.open_restaurant()



#Exercise 02
#Three restaurants:
class Restaurant: # i got invalid syntax here because i had not given colon after creating class.
    """Creating a class named Restaurant."""

    def __init__(self, restaurant_name, cuisine_type): #i got an invalid syntax here because i had not given space between def and __init__.
        """Initialize the restaurant's name and cuisine type."""
       
        self.restaurant_name = restaurant_name    # Store the values as instance attributes.We assign the value of the parameter restaurant_name to self.restaurant_name.-
        self.cuisine_type = cuisine_type             #-This creates an instance attribute, which is stored in the object.-
                                                      #-Every object created from the class gets its own restaurant_name and cuisine_type attributes.
    def describe_restaurant(self):  #self is a reference to the current object (instance), allowing the method to access that object's attributes and other methods.
        """Display the restaurant's name and cuisine type."""
       
        print(f"Restaurant name is {self.restaurant_name}")
        print(f"Cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        """Display a message indicating that the restaurant is open."""
       
        print(f"{self.restaurant_name} is OPEN.")

#Instance 01
restaurant = Restaurant('Meghana','Non-veg')

print(f"Restaurant {restaurant.restaurant_name}")
print(f"The cuisine is {restaurant.cuisine_type}")

# Call both methods.
restaurant.describe_restaurant()
restaurant.open_restaurant()

#Instance 02
italian_restaurant = Restaurant('Osteria','Italian cuisine')

print(f"Restaurant name: {italian_restaurant.restaurant_name}")
print(f"Cuisine type: {italian_restaurant.cuisine_type}")

italian_restaurant.describe_restaurant()

#Instance 03
french_restaurant = Restaurant('Plenitud','French cuisine')

print(f"Restaurant name: {french_restaurant.restaurant_name}")
print(f"Cuisine type: {french_restaurant.cuisine_type}")

french_restaurant.describe_restaurant()

#Instance 04
indian_restaurant = Restaurant('Quilon','Indian cuisine')

indian_restaurant.describe_restaurant()




#Exercise 03
#User

class User :
    """create a class User."""

    def __init__(self,first_name,last_name,user_id,age,country):
        """initialize parameters."""

        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.age = age
        self.country = country

    def describe_user(self):
        """User description."""

        print(f"User Details:")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"User ID: {self.user_id}")
        print(f"Age: {self.age}")
        print(f"Country: {self.country}")


    def greet_user(self):
        """Great the user.""" 
          
        print("Thank you for providing the details.")  
        print(f"Welcome Aboard {self.first_name} {self.last_name}.")
        print()  #This is gonna leave an empty line after every instance is printed.

#Instance 01
user_1 = User('Rakshitha','Kalingaiah','RK001',25,'India')
"""Create an Instance."""

#calling the two methods for this instance.
user_1.describe_user() 

user_1.greet_user()


#Instance 02
user_2 = User('Poojitha','Kalingaiah',"PK004",21,'India')

user_2.describe_user()

user_2.greet_user()

#Instance 03
user_3 = User('Yashwant','Anusuya','YA006',19,'India')

user_3.describe_user()

user_3.greet_user()


#Instance 04
user_4 = User('Siddharth','Anusuya','SA010',15,'India')

user_4.describe_user()

user_4.greet_user()


#Instance 05
user_5 = User('Dhanveer','Kannadiga','DK023',3,'India')

user_5.describe_user()

user_5.greet_user()



#Exercise 04
#Number served

#Explanation:
#In this exercise we will see three ways of modifying an attribute values.

#   METHOD 1:
#Changing the value directly through an instance and assigning a default value.
# Do not assign the default attribute in the __init__() method.
# Assign default attribute directly in the attributes.


class Restaurant:
    """Creating a class named Restaurant."""

    def __init__(self,restaurant_name,cuisine_type):  #when giving an default attribute we should not assign it in the init method.
        """Initialize the restaurant's name and cuisine type."""

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 200  #this is a Default attribute.

    def describe_restaurant(self):
        """Display the restaurant's name and cuisine type."""

        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")
        print(f"Number of people restaurant has served: {self.number_served}")

    def open_restaurant(self):
        """Display a message indicating that the restaurant is open."""

        print(f"{self.restaurant_name} is OPEN.")

restaurant = Restaurant('Meghana','Non-veg')
"""Create Instance"""

restaurant.describe_restaurant()
restaurant.open_restaurant()


#   METHOD 02:

class Restaurant:
    """Creating a class named Restaurant."""


    def __init__(self,restaurant_name,cuisine_type):  
        """Initialize the restaurant's name and cuisine type."""

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display the restaurant's name and cuisine type."""

        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")
        print(f"Number of people restaurant has served: {self.number_served}")

    def set_number_served(self, number_served):    #Here we created a parameter number_served.
        """Set the number of customers served."""

        self.number_served = number_served #and this tells python to replace parameter with the value we have called the function in.

    def open_restaurant(self):
        """Display a message indicating that the restaurant is open."""


restaurant = Restaurant('Meghana','Non-veg')
"""Create Instance"""

restaurant.describe_restaurant()
print()
restaurant.set_number_served(150) #this replaces the value 0 to 150.
restaurant.describe_restaurant()  
print()
restaurant.open_restaurant()


#Method 02:
#Example exercise
class Restaurant:
    """Creating a class named Restaurant."""


    def __init__(self,restaurant_name,cuisine_type):  
        """Initialize the restaurant's name and cuisine type."""

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.working_servers = 0

    def describe_restaurant(self):
        """Display the restaurant's name and cuisine type."""

        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")
        print(f"Working servers: {self.working_servers}")


    def servers(self,working_servers):

        self.working_servers = working_servers  


    def open_restaurant(self):
        """Display a message indicating that the restaurant is open."""


r_1 = Restaurant('Meghana foods','Non-veg')

r_1.describe_restaurant()
print()
r_1.servers(20)  #Remember always call the function with the attributes after modifying the value of an attribute through method. 
r_1.describe_restaurant()
r_1.open_restaurant()



#   METHOD 03:
#Modifying the attributes through increment.
class Restaurant:
    """Creating a class named Restaurant."""


    def __init__(self,restaurant_name,cuisine_type):  
        """Initialize the restaurant's name and cuisine type."""

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.working_servers = 0
        self.people_served = 6

    def describe_restaurant(self):
        """Display the restaurant's name and cuisine type."""

        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")
        print(f"Working servers: {self.working_servers}")
        print(f"Food served to people: {self.people_served}")

    def servers(self,working_servers):
        """Number of servers."""

        self.working_servers = working_servers  


    def served_food(self,people_served): #here we increment the people who have been served food.
        """Number of food served."""

        self.people_served += people_served #this takes the existing attribute value and if we assign new value to the parameter whenever we call the function-
                                               #-then it increment the total value.

    def open_restaurant(self):
        """Display a message indicating that the restaurant is open."""
       
        print("Restaurant's OPEN.")


r_1 = Restaurant('Meghana foods','Non-veg')

r_1.describe_restaurant()
r_1.open_restaurant()
print()
r_1.servers(20)  #Remember always call the function with the attributes after modifying the value of an attribute through method. 
r_1.served_food(40)  #here we are calling the served method.
r_1.describe_restaurant()
r_1.open_restaurant()
print()
r_1.servers(40)
r_1.served_food(60)
r_1.describe_restaurant()
r_1.open_restaurant()



#Exercise 05
#User

class User :
    """create a class User."""

    def __init__(self,first_name,last_name,user_id,age,country): 
        """initialize parameters."""

        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.age = age
        self.country = country
        self.login_attempts = 0 #Creating new attribute login_attempts.


    def describe_user(self):
        """User description."""

        print(f"User Details:")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"User ID: {self.user_id}")
        print(f"Age: {self.age}")
        print(f"Country: {self.country}")


    def increment_login_attempts(self):  #Method to increment login_attempts.
        """Method to increment the login_attempts."""
      
        self.login_attempts += 1 


    def reset_login_attempts(self): #method to reset the login_attempts.
        """Method to reset the login_attempts."""

        self.login_attempts = 0
    


    def greet_user(self):
        """Great the user.""" 
          
        print("Thank you for providing the details.")  
        print(f"Welcome Aboard {self.first_name} {self.last_name}.")
        print()  #This is gonna leave an empty line after every instance is printed.

#Instance 01
user_1 = User('Rakshitha','Kalingaiah','RK001',25,'India')
"""Create an Instance."""

#calling the two methods for this instance.
user_1.describe_user() 

user_1.increment_login_attempts()

print(f"Login attempts: {user_1.login_attempts}")

user_1.reset_login_attempts()

print(f"Login attempts after reset: {user_1.login_attempts}")

user_1.greet_user()



#Exercise 06
#IceCreamStand:
class Restaurant: # i got invalid syntax here because i had not given colon after creating class.
    """Creating a class named Restaurant."""

    def __init__(self, restaurant_name, cuisine_type): #i got an invalid syntax here because i had not given space between def and __init__.
        """Initialize the restaurant's name and cuisine type."""
       
        self.restaurant_name = restaurant_name    # Store the values as instance attributes.We assign the value of the parameter restaurant_name to self.restaurant_name.-
        self.cuisine_type = cuisine_type             #-This creates an instance attribute, which is stored in the object.-
                                                      #-Every object created from the class gets its own restaurant_name and cuisine_type attributes.
    def describe_restaurant(self):  #self is a reference to the current object (instance), allowing the method to access that object's attributes and other methods.
        """Display the restaurant's name and cuisine type."""
       
        print(f"Restaurant name is {self.restaurant_name}")
        print(f"Cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        """Display a message indicating that the restaurant is open."""
       
        print(f"{self.restaurant_name} is OPEN.")


class IceCreamStand(Restaurant):
    """Inherit class IceCreamStand fromclass Restaurant."""

    def __init__(self,restaurant_name,cuisine_type):
    
        """Calling super function."""
        super().__init__(restaurant_name,cuisine_type) #this allows me to use the init() method from parent class.  
        self.flavours = ['Vanilla','Strawberry','Chocolate','Butterscotch']  #adding a new default attribute. 


    def icecream_flavours(self):
        """Method contains list of icecream flavours."""
    
        print(self.flavours)


ice_cream = IceCreamStand('Meghana','Non-veg')
"""Instance of a child class IceCreamStand."""    


ice_cream.describe_restaurant()
ice_cream.icecream_flavours()  #calling the methos icecream _flavours.
ice_cream.open_restaurant()


#Exercise 07
#Admin:
class User :
    """create a class User."""

    def __init__(self,first_name,last_name,user_id,age,country):
        """initialize parameters."""

        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.age = age
        self.country = country

    def describe_user(self):
        """User description."""

        print(f"User Details:")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"User ID: {self.user_id}")
        print(f"Age: {self.age}")
        print(f"Country: {self.country}")


    def greet_user(self):
        """Great the user.""" 
          
        print("Thank you for providing the details.")  
        print(f"Welcome Aboard {self.first_name} {self.last_name}.")
        print()  #This is gonna leave an empty line after every instance is printed.

class Admin(User): #Child class of parent class User.
    """Creating a child class Admin."""

    def __init__(self,first_name,last_name,user_id,age,country): 
    

        super().__init__(first_name,last_name,user_id,age,country) #using superclass to get all functions of parent class.
        self.privileges = ['can add post',     #New attribute 
                           'can delete post',
                           'can ban user'
                           ]


    def show_privileges(self):
        """Method to show privileges."""

        print(self.privileges)


user = Admin('Rakshitha','Kalingaiah','RK001',25,'India')
"""Instance of an child class admin. """

user.describe_user()
print("These are the user privileges.")
user.show_privileges()
user.greet_user()


#Exercise 08
#Privileges:
class User :
    """create a class User."""

    def __init__(self,first_name,last_name,user_id,age,country):
        """initialize parameters."""

        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.age = age
        self.country = country

    def describe_user(self):
        """User description."""

        print(f"User Details:")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"User ID: {self.user_id}")
        print(f"Age: {self.age}")
        print(f"Country: {self.country}")


    def greet_user(self):
        """Great the user.""" 
          
        print("Thank you for providing the details.")  
        print(f"Welcome Aboard {self.first_name} {self.last_name}.")
        print()  #This is gonna leave an empty line after every instance is printed.



class Admin(User): #Child class of parent class User.
    """Creating a child class Admin."""

    def __init__(self,first_name,last_name,user_id,age,country): 
    

        super().__init__(first_name,last_name,user_id,age,country) #using superclass to get all functions of parent class.
        self.privileges = Privileges() #making an privileges instance as an attribute in the admin class.
                                      # This line tells Python to create a new instance of Privileges and assign that instance to the attribute self.privileges. 
                                        #This approach is called composition.


class Privileges:
     
    def __init__(self):
          
        self.privileges = ['can add post',    
                           'can delete post',
                           'can ban user'
                           ]

    def show_privileges(self):
        """Method to show privileges."""

        print(self.privileges)




user = Admin('Rakshitha','Kalingaiah','RK001',25,'India')
"""Instance of an child class admin. """

user.describe_user()
print("These are the user privileges.")
user.privileges.show_privileges()
user.greet_user()



#Exercise 09
#Battery upgrade:
class Car:

    def __init__(self,make,model,year):
        """Initialize attributes to describe a car."""

        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name.""" 
        
        long_name = f"{self.year} {self.make} {self.model}"       
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):    
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a fullcharge.")
    
    def upgrade_battery(self):
        """Method to update battery value."""
        if self.battery_size != 65:
            self.battery_size = 65
        else:
            print(f"this car ia already at 65 kwh.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.
           Then initialize attributes specific to an electric car."""
        
        super().__init__(make, model, year)
        self.battery = Battery()


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
print()
my_leaf.battery.upgrade_battery()
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()



#Exercise 10
#Dice:

from random import randint

#This is a 6 sided die and we are rolling it 10 times.

class Die:
    """Create a class called Die"""

    def __init__(self, sides=6):
        """initialize attribute with a default number."""
        self.sides = sides

    def roll_die(self):
        """Roll the die between 1 to 6 """
        print(randint(1,self.sides))


die = Die() 
"""Instance of class Die."""

print("rolling a six sided die. ")
for roll in range(10):
    die.roll_die()



#Exercise 11
#Lottery:

from random import choice

tickets = [2,'V',6,4,8,0,3,9,'E','T','I','D',5,1,7]

first = choice(tickets)
print(first)

second = choice(tickets)
print(second)

third = choice(tickets)
print(third)

fourth = choice(tickets)
print(fourth)


print("Any tickets matching these given words or numbers wins a prize.")


# Exercise 12
# Lottery Analysis:

from random import choice

# List of possible lottery values
tickets = [2, 'V', 6, 4, 8, 0, 3, 9, 'E', 'T', 'I', 'D', 5, 1, 7]

# Your lottery ticket
my_ticket = [2, 'V', 'D', 8]

attempts = 0

while True:
    # Generate a random winning ticket
    winning_ticket = [
        choice(tickets),
        choice(tickets),
        choice(tickets),
        choice(tickets)
    ]

    attempts += 1

    # Check if the tickets match
    if winning_ticket == my_ticket:
        print("🎉 Congratulations! Your ticket won!")
        print(f"Winning ticket: {winning_ticket}")
        print(f"It took {attempts} attempts to win.")
        break
