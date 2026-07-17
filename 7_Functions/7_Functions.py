#Message
#Exercise 01: 
def display_message(): #here we have defined a function named display_message.
    print("I am learning about functions and how all we can use a function in python.") #this is the body of the function 
                                                                #and this is what we want the function to say or run whenever we call the function display_message.
display_message() #here we are calling the function.


#Favourite book
#Exercise 02:
def favourite_book(favouritebook): #here we have given one parameter which is favouritebook
    print(f"My favourite book is {favouritebook.title()}")   


favourite_book('king of wrath') #here the king of wrath is an argument.

favourite_book('reign of king') #here reign of king is an argument.


#T-Shirt
#Exercise 03:
#Version 01: # this is positional 
def make_shirt(shirt_size, shirt_message):
    print(f"\nthe shirt size is {shirt_size}")
    print(f"the text on the shirt will be: {shirt_message}")

make_shirt('L','Aut viam inveniam aut faciam')

#Version 02:
def make_shirt(shirt_size, shirt_message):
    print(f"The shirt size is: {shirt_size}")
    print(f"The message on the shirt is: {shirt_message}")

make_shirt(shirt_size='Large', shirt_message='Aut viam inveniam aut faciam.')


#Exercise 04:
#Large_shirt
#Version 01: here we are setting the large as the default parameter for size and here we are using Default value to do that.
def make_shirt(shirt_message, shirt_size='Large'):
    print(f"\nthe shirt size is {shirt_size}")
    print(f"the text on the shirt will be: {shirt_message}")

make_shirt('I love python.')


#Version 02: here we have given both the parameters the default value.

def make_shirt(shirt_size='Large and Medium', shirt_message= 'Sorry we are out of these sizes'):
    print(f"\nshirt size: {shirt_size}")
    print(f"{shirt_message}")

make_shirt()

def make_shirt(shirt_size='small', shirt_message= 'Ilove python'):
    print(f"\nshirt size: {shirt_size}")
    print(f"{shirt_message}")

make_shirt()


#Exercise 05:
#Cities

def describe_city(city, country='Greece'):
    print(f"{city} city, is located in {country}")

describe_city('banglore','india')
describe_city('chania')
describe_city('nafplio')


#Exercise 06:
def formatted_name(first_name, last_name):

    full_name = (f"{first_name} {last_name}")
    return full_name.title()
fullname = formatted_name('rakshitha', 'kalingaiah')
print(fullname)


#Exercise 07
#City names:
def city_country(city,country):

    country =(f"{city} {country}")
    return country.title() #here we have used return value.

country = city_country('banglore','india')
print(country)
 
country = city_country('rome', 'italy')
print(country)

country = city_country('nafplio', 'greece')
print(country)


#Exercise 08:
#Album
#Version 01:
def make_album(artist_name,album_title):
    music_album = {'artist_name': artist_name,'album_title': album_title}                   

    return music_album

Music_album = make_album('Taylor swift','Daylights')
print(Music_album)

Music_album = make_album('Taylor swift','Gorgeous')
print(Music_album)

Music_album = make_album('Taylor swift','Dress')
print(Music_album)


#Version 02: in this we have optional parameter None
def make_album(artist_name,album_title,num_of_songs = None): #here we are using an optional parameter None
    music_album = {                                         #always create a dictionary first if you are using one
        'artist_name': artist_name,
        'album_title': album_title,
    }
    if num_of_songs is not None:         #this is the whole condition of the code it says if the num of songs key gets a pair other than None then print it,
        music_album['num_of_songs'] = num_of_songs       #if not only print artist name and album title.
    else:
        music_album = {'artist_name': artist_name, 'album_title': album_title}                   

    return music_album

music_album = make_album('Taylor swift','Daylights')
print(music_album)

music_album = make_album('Taylor swift','Gorgeous')
print(music_album)

music_album = make_album('Taylor swift','Dress')
print(music_album)

music_album = make_album('Tylor swift','Look what you made me do',4)
print(music_album)


#Exercise 09:
#User albums    
#in this code we have used while loop
def make_album(artist_name, album_title, num_of_songs=None):
    music_album = {
        'artist_name': artist_name,
        'album_title': album_title,
    }

    if num_of_songs:
        music_album['num_of_songs'] = num_of_songs

    return music_album


while True:
    artist_name = input("Artist name (or 'quit' to exit): ")
    if artist_name == 'quit':
        break

    album_title = input("Album title (or 'quit' to exit): ")
    if album_title == 'quit':
        break

    album = make_album(artist_name, album_title)
    print(album)


#Exercise 10:
#Messages
text_messages = ['hello','hi','hola','chao'] #always write the list first.

def show_messages(messages): #when using list with a function make sure you give a parameter in a finction. here the parameter is (messages)
    for message in messages:
        print(message)

show_messages(text_messages)


#Exercise 11
#Sending messages:
text_messages = ['hello','hi','hola','chao']
sent_messages = []

def send_messages(messages):
    while messages:
        message = messages.pop()
        print(message)
        sent_messages .append(message) 
        
send_messages(text_messages)

print(f"\nSent messages: {sent_messages}")
print(f"Text messages: {text_messages}")

#in here we use a parameter (messages) why because instead of this if we had used text_messages,
#we will not be able to use any other list other than text_messages.
#One thing to remember: The parameter name can be anything.
#So the important part is not the name messages, but the fact that it's a parameter that receives whatever list you pass to the function.

#Exercise 12
#Archived messages:
#we are adding slice to make a copy of the original list and the loop,pop,append works on the copied list the original list stays intact. 
text_messages = ['hello','hi','hola','chao']
sent_messages = []

def send_messages(messages):
    while messages:
        message = messages.pop()
        print(message)
        sent_messages .append(message) 
        
send_messages(text_messages[:]) #here slice makes a copy of the original list and works on that list  

print(f"\nSent messages: {sent_messages}")
print(f"Text messages: {text_messages}")


#Exercise 13
#Sandwiches
def sandwiches(*fillings):
    for filling in fillings:
        print(filling)

print("Here are the requested fillings: ")

sandwiches('cheese')
sandwiches('tomato','onion')
sandwiches('avacado','seasame seeds','salt')

#Explanation:
#in line 3 we are defining a function named sandwiches and *args - which tells the python to save all the parameters that user gives in the tuple called fillings.
# in line 4 we are writting for loop for the python to go through all the parameters saved in the tuple fillings.
# in line 9,10,11, we are calling the function with multiple parameters and and all the parameters will be saved in an single tuple (fillings).
# in these we use tuples not lists because arguments are only to be read not modified. 
# and tuples cannot be modified.


#Exercise 14
#User profile:
def build_profile(first,last,**user_profile):
    user_profile['first_name'] = first
    user_profile['last_name'] = last
    return user_profile

user_profile = build_profile('Rakshitha','Kalingaiah',
                             Country= 'India',
                             City = 'Banglore')

print(user_profile)

#Explanation:
#in line 3 python expects first and last name and allows the user to give as much of the information in key value pairs in the user_profile.
# the double asterisks(**) tells python to create a dictionary to save the key value pairs given by the user.
# in line 4,5, we are adding the first and last name to the user_profile because it wasn't added yet.
# in line 6 we are returning the user_profile dictionary to call line function.
# in line 8 we are assinging the values of build_profile to user_profile.
# in line 12 we are printing all the values the user_profile contains.

#Exercise 15
#Cars:
def cars_info(manufacturer,model_name,**optional_offers):
    optional_offers['manufacturer'] = manufacturer
    optional_offers['model_name'] = model_name
    return optional_offers

optional_offers = cars_info('BMVV','M3',
                            color = 'Matt black',
                            tow_package = 'No')

print(optional_offers)

optional_offers = cars_info('ferrari','f1',
                             color = 'Red',
                             tow_package = 'True')

print(optional_offers)