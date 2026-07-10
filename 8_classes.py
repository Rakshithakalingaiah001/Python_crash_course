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