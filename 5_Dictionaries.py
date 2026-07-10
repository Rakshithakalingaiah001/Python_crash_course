#Exercise 1: Person detail

#Dictionaries can be defined in two ways:
#Version 01:
Rakshitha = {
    'First_name': 'Rakshitha', 
    'Last_name': 'kalingaiah', 
    'Age': 25, 
    'City': 'Banglore',
}
print(f"Details of Rakshitha")
print(f"First name:",Rakshitha['First_name'])
print(f"Last name:",Rakshitha['Last_name'])
print(f"Age:",Rakshitha['Age'])
print(f"City:",Rakshitha['City'])


#Version 02:
Rakshitha = {'First_name': 'Rakshitha','Last_name': 'kalingaiah', 'Age': 25, 'City': 'Banglore',}
print(f"Details of Rakshitha")
print(f"First name:",Rakshitha['First_name'])
print(f"Last name:",Rakshitha['Last_name'])
print(f"Age:",Rakshitha['Age'])
print(f"City:",Rakshitha['City'])


#Exercise 2: Favourite numbers

#Version 01:
Favourite_num = {
    'Raksha': '13',
    'Pooja': '23',
    'Yashu': '12',
    'Siddhu': '19',
    'Dhanveer': '3',
}
print("Your friends and their favourite numbers:")
print(f"Raksha:",Favourite_num['Raksha'])
print(f"Pooja:",Favourite_num['Pooja'])
print(f"Yashu:",Favourite_num['Yashu'])
print(f"Siddhu:",Favourite_num['Siddhu'])
print(f"Dhanveer:",Favourite_num['Dhanveer'])

#Version 02:
Favourite_num = {
    'Raksha': [13, 2001],
    'Pooja': [23, 2004],
    'Yashu': [12, 2006],
    'Siddhu': [19, 2010],
    'Dhanveer': [3, 2023],
}
print("Your friends and their favourite numbers:")
print(f"Raksha:",Favourite_num['Raksha'])
print(f"Pooja:",Favourite_num['Pooja'])
print(f"Yashu:",Favourite_num['Yashu'])
print(f"Siddhu:",Favourite_num['Siddhu'])
print(f"Dhanveer:",Favourite_num['Dhanveer'])


#Exercise 3: Glossary

Glossary = {
    'Dictionaries': 'it is a collection of key and value pair',
    'if': 'if is an condition statement.',
    'in and not in': 'These are membership operators.',
    'indentation': 'this means space.',
    'Square braces': '[] these are square braces.',
}

print(f"Dictionary: \n",Glossary['Dictionaries'])
print(f"\nif: \n",Glossary['if'])
print(f"\nin and not in:\n ",Glossary['in and not in'])
print(f"\nindentation: \n",Glossary['indentation'])
print(f"\nSquare braces: \n",Glossary['Square braces'])

#here output prints like:

#Dictionaries:
#it is a collection of key and value pair.


#Looping through a dictionary.
#Exercise 4:
Glossary = {
    'Dictionaries': 'it is a collection of key and value pair',
    'if': 'if is an condition statement.',
    'in and not in': 'These are membership operators.',
    'indentation': 'this means space.',
    'Square braces': '[] these are square braces.',
    'For loop': 'for loop is used when we want to run some condition or a statement for a fixed number of time.',
    'Nesting': 'we use nesting loop to loop one loop inside another loop, like for loop inside while or vise versa.',
    'f string': 'we use f string when we want to use varibles with values inside a string.',
    'variables': 'we store a date or any value inside a varible.',
    'string': 'a series a letters written inside a double inverted commas are strings.',
}

for k , v in Glossary .items():  #when using for loop .items() is important for the for loop to lopp through the dictionary.
    print(f"\n {k}: {v}")

#Exercise 5:
Rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china',
}

for key , value in Rivers .items():
    print(f"the {key} river runs through {value}")


#using for loop to only print the keys in the dictionary. 
Rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china',
}

for river in Rivers .keys():   #here using the for loop we are printing only keys and not their values.
    print(f"{river}")
print("these are the major rivers in the world.") 


#Using for loop to print only the values.
Rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china',
}

for river in Rivers .values(): #here by using .values() we are only printing the values from a dictionary.
    print(f"{river}")
print("these are the countries the major rivers flow through.")

#Polling 
#Exercise 6:
Favourite_languages = {
    'R': 'Python',
    'P': 'C',
    'Y': 'C++',
    'S': 'Rust',
    'D': 'Python',
}

people = ['N', 'A', 'G', 'L', 'P', 'R', 'Y', 'S', 'D']

for person in people:
    if person in Favourite_languages:
        print(f"Thank you {person} for taking the favourite languages poll.")
    else:
        print(f"{person}, please take the favourite languages poll.")


#Exercise 7:

Rakshitha = {
    'First_name': 'Rakshitha', 
    'Last_name': 'kalingaiah', 
    'Age': 25, 
    'City': 'Banglore',
}

Poojitha = {
    'First_name': 'poojitha',
    'Last_name': 'Nagamani',
    'Age': 21,
    'City': 'Banglore',
}

Yashwanth = {
    'First_name': 'Yashwanth',
    'Last_name': 'Anusuya',
    'Age': 19,
    'City': 'Banglore',
}

people = [Rakshitha, Poojitha, Yashwanth]

print("Details of people:")
for peoples in people:
    print(f"\nFirst name: {peoples['First_name']}")# here {peoples} is a dictionary and [First_name] is a key which has a value. 
    print(f"Last name: {peoples['Last_name']}")
    print(f"Age: {peoples['Age']}")
    print(f"City: {peoples['City']}")



#Exercise 8:

Coco = {
    'Pet name': 'Coco',
    'Animal': 'Dog',
    'Owner name': 'Pooja',
}

Tizan = {
    'Pet name': 'Tizan',
    'Animal': 'Dog',
    'Owner name': 'Yashu',
}

Pets = [Coco, Tizan] #here the Pets becomes a dictionary. so pet == coco and tizan

for pet in Pets:
    print(f"\nPet name: {pet['Pet name']}") #here "Pet name" is a string. {pet} is a dictionary, ['Pet name'] is a key in the dictionary.
    print(f"Animal: {pet['Animal']}")
    print(f"Owner name: {pet['Owner name']}")

#Explanation: 
#here coco and tizan are two dictionaries that contains details about pets in the key value pair.
#Pets = [coco , tizan] this is list in which we have stored our two dictionaries.
# for pet in Pets:
# in for loop pet is a variable we are creating to store the looped statements and we are looping Pets variable which is list storing a dictionaries.
#we use [] whenever we need a value of key.

#Exercise 9:
Favourite_places = {'Rakshitha': 'London', 'Pooja': 'Spain', 'Yashu': 'Japan',}

for key , value in Favourite_places .items():
    print(f"{key}'s favourite place is {value}")
    

#Exercise 10: 
#Cities:
greece = {
    'city': 'nafplio',
    'country': 'greece',
    'population': '10 million',
    'fact': 'longest coastaline in the mediterian sea.',
}

italy = {
    'city': 'rome',
    'country': 'italy',
    'population': '57.9 million',
    'fact': 'lot of ancient history',
}

fiji = {
    'city': 'savusavu',
    'country': 'fiji',
    'population': '7000',
    'fact': 'charming coastal town.'
}

Cities = [greece, italy, fiji]

for cities in Cities:
    print(f"\ncity: {cities['city']}")
    print(f"country: {cities['country']}")
    print(f"population: {cities['population']}")
    print(f"fact: {cities['fact']}")

##iMPORTANT NOTE:
# remember after the for loop when writting the print statements always write the dictionary name inside the flower braces and inside them write the key of the 
#  value you need.

#Exercise 11:
#Extensions:
Favourite_places = {
    'Rakshitha': 'London', 
    'Pooja': 'Spain', 
    'Yashu': 'Japan',
    'Siddhu': 'New york',
    'Dhanveer': 'italy',   
}

for key , value in Favourite_places .items():
    print(f"{key}'s favourite place is {value}")

#added two more pair of key and value.

###END OF DICTIONARY CHAPTER AND EXERCISES.