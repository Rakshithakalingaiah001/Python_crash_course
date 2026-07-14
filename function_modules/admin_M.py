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



#"from admin_M import User"  when we have splitted classes that are dependent on another or parent class we should always import the parent class to the module
                                                                          # where we have stored a child class.
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
