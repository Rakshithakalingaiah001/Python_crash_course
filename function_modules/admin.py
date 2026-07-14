from admin_M import Admin


user = Admin('R','K','RK',25,'I')


user.describe_user()
user.privileges.show_privileges()
user.greet_user()


#while importing the module admin_M,
#the mistake i made is i called the User class but i should call the Admin class which has both the privileges attribute and the user class functions.
