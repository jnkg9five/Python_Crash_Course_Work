#Dictionaries
#PYTHON CRASH COURSE Chapter#6

#We will use Python's dictionaries, or associative array, which allow to connect pieces of related information.
#You will learn to access the information in a dictionary.
#Dictionaries can store an almost limitless amount of information. 
#You will learn that you can nest dictionaries inside lists, list inside dictionaries, and dictionaries inside other dictionaries.

#Understanding dictionaries allows you to model a variety fo real-world objects more accurately. 
#You can store a persons information about their name, age, location, profession, etc.
#You can store any two kinds of information that can be matched up, such as a list of words and their meanings.
#Lists of mountains, their elevations, locations, and climate.

#A Simple Dictionary

#Consider a game featuring aliens that have different colors and point values
#The simple dictionary stores information about an alien.

alien_0 = { 'color' : 'green' , 'points' : 5}

print(alien_0['color'])
print(alien_0['points'])

#The dictionary alien_0 stores the alien's color and point value. 

###############################
## WORKING WITH DICTIONARIES
###############################
#A dictionary in Python is a collection of key-value pairs.
#Each key is connection to a value. The key is used to get access to a value associated with that key.
#A key's value can be a string, a list, or another dictionary. 
#You can use any object in Python as a dictionary value.
#A dictionary in Python is wrapped in braces, {}, with a series of key-value pairs inside the braces.

auto_book = {'cars' : 'bugatti' , 'horsepower' : '1500hp'}

#The simplest dictionary has exactly on key-value pair.

alien_1 = {'color': 'pink'}

#Accessing Values in a Dictionary
#To get access to values associated with a key, pit the name of dictionary and the place the key inside set of square brackets.

print(alien_1['color'])

#You can have an unlimited number of key-value pairs in a dictionary.
#For alien_0, you can lookup how many points a player should get after hitting an alien.

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")


###############################
## Adding New Key-Value Pairs
###############################

#Dictionaries are dynamic structures
#You can add new key-value pairs at any times in a dictionary.
#The the previous alien example, lets att two new pieces of information.
#Let's add the alien's x and y coordinates, in will help display an alien in a particular position on a screen.
#We will place the alien on the left edge of the screen, 25 pixels down form the top. Screen coordinates usually start at the upper-left corner of the screen.
#The alien will be placed on the left edge of teh screen.
#We will set the x-coordinate to 0 and the y-coordinate to positive 25.

print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#We start by printing the original dictionary, to display the existing key-value pairs.
#Then we add a new key-value pairs to the dictionary, one each for x and y coordinates.
#The final version of the dictionary has 4 key-value pairs now. The order of the pairs does not care about the order in which you store the key-value pairs.
#The dictionary only cares about the connection between a key and its value.

#Starting with an empty dictionary.
#It's sometimes convention or necessary to start an empty dictionary and then add each new key-value pair to it.
#To define an empty dictionary, start with assigning a dictionary to set of empty set of braces {}.

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

#The above shows how to start from an empty dictionary and add to the dictionary.
#Typically you use empty dictionaries when storing -user-suppled data or you write code that generates large numbers of key-value pairs automatically.

#Modifying Values in a Dictionary 
#################################################
#To modify a value in a dictionary, give the name of the dictionary with the key in square brackets and then the new value you want associated with the key. 

#Lets consider an alien that changes from green to yellow as the game continues.

alien_0 = {'color' : 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

#The example we used above changes the original color key with value green to value yellow for the same key.

#For a more interesting example, let's track the position of an alien that is moving at different speeds.
#We store a value representing the alien's current speed and the use it to determine how far right eh alien should move.

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position" + str(alien_0['x_position']))

# Move the alien to the right
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #This must be a fast alien
    x_increment = 3
    
#The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

#The output will be a new x-position of 2 based on the key-value pairs for speed which is medium. 
#In the if elif else chain, the medium condition will set x_increment to 2. 
#Then the value in the key-value pair is modified.

#Removing Key-Value Pairs.
################################

#Lets say you no longer need a key-value pair piece in a dictionary, you can use the del statement to completely remove a that key-value pair.
#The example below is how to remove the key along with its value.

alien_0 = {'color':'green','points':5}
print(alien_0)

del alien_0['points']
print(alien_0)

#The line using the del statement tells Python to delete the key 'points' from the dictionary and remove the associate value with that key.
#Be aware that deleted key-value pair is removed permanently. 


####################################
#A Dictionary of Similar Objects
####################################

#The previous example of storing different kinds of information about one object, an alien in a game.
#You can also use dictionaries to store one kind of information about multiple objects.
#Say you want to poll oa number of people and ask what their favorite programming language is.

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

#The dictionary is broken into several lines. 
#Each key is a name of a person who responded to the poll, and each value is the programming language choice.
#When you know you will need more than 1 line to define a dictionary,, press ENTER after the opening brace.
#It's good practice to include a comma after the last key-value pair as well, so you're ready to add a new key-value pair on the next line. 

#To use the dictionary, given the name of the person who took the poll, you can look up their favorite programming language.
print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")


#####################################
#Practice Try it Yourself Problems
#####################################

#Person: Use a dictionary to store information about a person you know.
#Store their first name, last name, age and city in which they live. 
#You should have keys such as first-name, last_name, age, and city.
#Print each piece of information stored in your dictionary.

Person = {
    'first_name' : 'Junjie',
    'last_name' : 'Li',
    'age' : '33',
    'city' : 'Trenton',
} 

print("The person's first name is " + Person['first_name'] + ".")
print("The person's last name is " + Person['last_name'] + ".")
print("The person's age is " + Person['age'] + ".")
print("The city the person lives is " + Person['city'] + ".")


#Favorite Numbers: Use a dictionary to store people's favorite numbers.
#Think of 5 names, and use them as keys in your dictionary. Think of a favorite number for each person.
#Store each as a value in your dictionary
#Print each person's name and their favorite number.

Favorite_Numbers = {
    'Logan'  : 'twelve' ,
    'Paul' : 'hundred' ,
    'Dan' : 'one' ,
    'Josh' : 'fifty' ,
    'Loco' : 'nine' ,
}

print("Logan's favorite color is" + Favorite_Numbers['Logan']  )
print("Paul's favorite color is" + Favorite_Numbers['Paul']  )
print("Dan's favorite color is" + Favorite_Numbers['Dan']  )
print("Josh's favorite color is" + Favorite_Numbers['Josh']  )
print("Loco's favorite color is" + Favorite_Numbers['Loco']  )

#Glossary: A Python dictionary can be used to model and actual dictionary.
#Call it a glossary. 

#Think of five programming words learned the previous chapters. 
#Use the words as the keys in the glossary and store their meaning as values.
#Print each word and its meaning. 

Glossary = {
    'List' : 'A set of stored elements' ,
    'Equality' : 'A conditional tests that compares two value' ,
    'If_Statement' : 'A conditional tests that executes if true else the negate condition is executed',
    'Dictionary' : 'Pieces of information that are related connected together',
    'Variable' : 'Data that is stored under a unique identifier',
}

print("\nList is " + Glossary['List'])
print("\nEquality is " + Glossary['Equality'])
print("\nIf_Statement is " + Glossary['If_Statement'])
print("\nDictionary is " + Glossary['Dictionary'])
print("\nVariable is " + Glossary['Variable'])


###################################
## Looping Through a Dictionary
###################################

#A single Python dictionary can have a few key-value pairs or millions of pairs.
#Because a dictionary can contain large amounts of data,  you can loop though a dictionary.
#Dictionaries can be used to store information in a variety of ways; There are several ways to loop through dictionaries.
#You can loop through all of a dictionary's key-value pairs, through keys, or its values.

#LOOPING THROUGH All key-value pairs.

#Before we explore the different approaches to looping. Lets have a new dictionary designed to store information.
#The keys are about a user on a website. 
#The dictionary stores the username, first name, and last name.

user_0 = {
    'username' : 'efermi', 
    'first' : 'enrico',
    'last' : 'fermi',
}

#What if you wanted to see everything stored in the user dictionary?
#You can loop though the dictionary using a for loop:

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

#When writing a for loop for a dictionary, you create two variable names that will hold the key and the value in each key-value pair.
#You can choose any names since these are temp variables only used the the for loop. 
#The for statement includes the name of the dictionary plus the method items(), which returns a list of key-value pairs.
#The for loop stores each of these pairs in the two variables provided.

#In the preceding example, we use variables to print each key then the associated value. 
#Note key-value pairs are not returned in the order they are stored, even when looping. Python does not look at order, only the key-value pairs.

#Looping for all key-value pairs works well for long dictionaries like favorite_languages.py

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + 
        language.title() + ".")

#This looping will work for a poll of thousands or even millions of people.

#Looping Through All the Keys in a dictionary
###############################################

#The keys() method is useful when you don't need to work with all the values in a dictionary. 
#Lets print the names of everyone who took the poll:

for name in favorite_languages.keys():
    print(name.title())

#Looping through keys is the default behavior in Python when looping in a through a dictionary.

for name in favorite_languages:
    print(name.title())

#You can access the value associated with any key you care about inside the loop by using the current key.
#Let's print a message to a couple of friends, about the languages they choose.

#The algorithm that will be used is to loop through the names in the dictionary.
#Then when the name matches one of our friends, we'll display a message about their favorite language.

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends: #check if the name of your friends are found.
        print(" Hi " + name.title() +
            ", I see your favorite language is " + 
            favorite_languages[name].title() + "!") #name key will get the paired value associated with your friend.

#You can use the keys() moethod to find if a particular person was not polled

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

#Looping Through Dictionary Keys in Order
#############################################

#A dictionary always maintains a clear connection between key and its associated value. 
#You will not et items from a dictionary in any oder.
#One way to return items in certain order is to sort the keys as they are returned from the for loop.
#Use the sorted() function to get the keys in order.

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

#We wrapped the sorted() methods around the dictionary.keys() method to get the list of key-value pairs in order.
#For example, if we want list of all languages chosen in the programming poll, we can do the follow. 

print("The following languages have been mentioned: ")
for language in favorite_languages.values():
    print(language.title())

#This will pull all the values from the dictionary without checking for repeats. 
#This may work find with a small set of values. But with a larger poll, there will be many repeat values.
#TO see each language chosen without repetition, we can use a set.  

print("The following languages have been mentioned: ")
for language in set(favorite_languages.values()):
    print(language.title())

#When using the set() method around a dictionary list with duplicate values, 
#Python identifies the unique times in the list and builds a set from those items. 
#The result is a not repetitive list. 

#As you continue learning with Python, you'll find built-in features of the language that will helps with your program logic.

############################
## TRY IT YOURSELF EXERCISES
############################

#Glossary 2
#Clean up the code from the previous try it yourself exercises
#Replace the series of print repetitions wih a loop that runs through the dictionary.

#Person = {
#    'first_name' : 'Junjie',
#    'last_name' : 'Li',
#    'age' : '33',
#    'city' : 'Trenton',
#} 

for category, persons in Person.items():
    print("The person's " + category + "is " + persons.title() + ".")

#Favorite_Numbers = {
#    'Logan'  : 'twelve' ,
#    'Paul' : 'hundred' ,
#    'Dan' : 'one' ,
#    'Josh' : 'fifty' ,
#    'Loco' : 'nine' ,
#}

for category, numbers in Favorite_Numbers.items():
    print( category.title() + "'s favorite color is" + numbers.title() + ".")

#Glossary = {
#    'List' : 'A set of stored elements' ,
#    'Equality' : 'A conditional tests that compares two value' ,
#    'If_Statement' : 'A conditional tests that executes if true else the negate condition is executed',
#    'Dictionary' : 'Pieces of information that are related connected together',
#    'Variable' : 'Data that is stored under a unique identifier',
#}

for category, meta in Glossary.items():
    print("\n " + category.title() + " is " + meta.title())

#RIVERS
#Make a dictionary with three major rivers and the country ech river runs through.

#Use a loop to print a sentence about each river.
#Use a loop to print the name of each river included in the dictionary. 
#Use a loop to print the name of each country included in the dictionary.

river_location = {
    'nile':'egypt',
    'mississippi':'USA',
    'thames':'united_kingdom',
    'yangtze':'chine',
    'euphrates':'syria',
}

for category, meta in river_location.items():
    print("\nThe country " + category.title() + " has the major river " +meta.title() + " running through there.")

#Polling

#Make a list of people who should take the favorite language poll. 
#Include the names that are in the dictionary: favorite languages. 
#Loop through the list of people who should take the poll. 
#If they already have taken the poll print a message thanking them for responding.
#If they have not taken the poll, print a message inviting them to take the poll.

#favorite_languages = {
#    'jen' : 'python',
#    'sarah' : 'c',
#    'edward' : 'ruby',
#    'phil' : 'python',
#}

favorite_languages_people = ['jen','harry','edward','phil']
n = 0

for meta in favorite_languages.keys():
    if meta == favorite_languages_people[n]:
        print("Thank you, " + favorite_languages_people[n].title() + " for taking the poll!")
        n += 1
    else:
        print("You, " + favorite_languages_people[n].title() + ", are invited to take the poll.")
        n += 1

################################
## NESTING
################################
print("\n")
#Sometimes you want ot store a set of dictionaries in a list or list of elements as a value in dictionary.
#This is called nesting. 
#You can nest a set of dictionaries in a list, a list of elements in a dictionary, or dictionary in another dictionary. 

#The following example is an example of nesting. 
#The previous alien_0 dictionary in the beginning of the chapter contained a variety of information about one alien.
#How about a second alien, or a screen full of aliens. 
#How can you manage a fleet of aliens. One way is to make a list of aliens which each alien is a dictionary of information about that alien.
#For example, the following code builds a list of three aliens:

#First, we create the three dictionaries, one for a different alien, and pack the dictionaries into a list called aliens.
#You can then loop through the list and print out each alien:

alien_0 = {'color':'green','points':'5'} 
alien_1 = {'color':'yellow','points':'10'}
alien_2 = {'color':'red','points':'15'}  

aliens = [alien_0,alien_1,alien_2]

for alien in aliens:
    print(alien)


print("\n")
#A more applicable example would involve more than 3 aliens, and code that automatically generates each alien.
#The following example uses the range() function to create a fleet of 30 aliens:

#Make an empty list for storing aliens.
aliens = []
for alien_number in range(30): #Make 30 green aliens
    new_alien = {'color':'green', 'points':'5', 'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]: #show the first 5 aliens by slicing list
    print(alien)
print("...")

print("Total number of aliens: " + str(len(aliens))) #Show how many aliens have been created.

#The above example starts with an empty list to have all the alien dictionaries be appended.
#The range() function returns a set of numbers to tell Python how many times we want the for loop to repeat. 
#Each time the loop runs, it creates a new alien with the dictionary defined by new_alien. 
#Then to check the results for the first five aliens, we use a list slice [:5] to show the first five dictionary for the first 5 aliens.

#The aliens all have the same characteristics defined by the new_alien dictionary in the for loop.
#Python however consideres each one a separate object, which allows to modify each alien individually.
#How might you work with a set of aliens like this. 
# #Imagine a game has some aliens changing colors and moving faster as the game progresses.
# When it is time to colors, we can use a for loop and if statement to change the colors of the aliens.

#We can change the first three aliens to yellow, medium-speed aliens worth 10 points each, by doing the following.
print("\n")
#aliens = []
#for alien_number in range(30): #Make 30 green aliens
#    new_alien = {'color':'green', 'points':'5', 'speed':'slow'}
#    aliens.append(new_alien)

for alien in aliens[0:3]: #For loop to modify the dictionary values for color, speed, and points based on condition for color : green
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[:5]: #show the first 5 aliens by slicing list
    print(alien)
print("...")

print("Total number of aliens: " + str(len(aliens))) #Show how many aliens have been created.

#The new for loop above will modify only the first 3 green aliens. 
#You can expand the loop by adding an elif block that turns yellow aliens into red, fast-moving one worth 15 points each.
print("\n")
#aliens = []
#for alien_number in range(30): #Make 30 green aliens
#    new_alien = {'color':'green', 'points':'5', 'speed':'slow'}
#    aliens.append(new_alien)

for alien in aliens[0:3]: #For loop to modify the dictionary values for color, speed, and points based on condition for color : green
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = '15'

for alien in aliens[:5]: #show the first 5 aliens by slicing list
    print(alien)
print("...")

print("Total number of aliens: " + str(len(aliens))) #Show how many aliens have been created.

#It is common to store a number of dictionaries in a list when each dictionary contains many kinds of information about one object.
#For example you might create a dictionary for each user on a website. (name, age, location, ethnicity, gender, height)
#All the dictionaries in the list should have an identical structure so you can loop through the list.
#This way you can with each dictionary object in the same way.  

#A List in a Dictionary
################################

#Now lest put a dictionary inside a list. It's sometimes useful to put a list inside a dictionary. 
#For example, consider how you might describe a pizza that someone is ordering.
#If you only use a list, all yo can store is a list of pizza's toppings. 
#With a dictionary, a list of toppings can be just obe aspect of the pizza.

#For example, two kinds of information are stored for each pizza, type of crust and a list of toppings.
#The list of toppings is a value with the key 'toppings'.
#To use the elements in the list, we give the name of the dictionary, and the key 'toppings'.
#Instead of returning a single value, we get a list of toppings:

pizza = { #Store information about pizza for an order. 
    'crust': 'thick',
    'toppings' : ['mushrooms', 'extra_cheese']
}

print("You ordered a " + pizza['crust'] + "-curst pizza" + 
        "with the following toppings:") #Prompt on the type of crust ordered
for topping in pizza['toppings']: #for loop to prompt the list of toppings ordered
    print("\t " + topping)

#The example above starts with a dictionary named pizza, that holds information about a pizza that has been ordered.
#The one key in the dictionary is 'crust' type. 
#The associated value for the 'crust' is 'thick'.
#The next key is the toppings.

#Then the output is summarized with the type of crust and the toppings from the pizza dictionary.
print("\n")

#You can nest a list inside a dictionary. 
#Any time you want more than one value to be associated with a single key in a dictionary. 
#From the favorite programming languages examples, we can store the value associated with each person would be a list of languages.
#Inside the dictionary for loop. 
#We can use another for loop to run through the list fo languages associated with each person.

favorite_languages = {
    'jen' : ['python','ruby'],
    'sarah' : 'c',
    'edward' : ['ruby','go'],
    'phil' : ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())

#The example above, the value associate with each name, is now a list.
#Some of the names listed have more than one favorite langauge.
#When you loop through the dictionary, we use temp variable languages to hold each value from the dictionary.
#This is because each value will be a list. 

#Then inside the main dictionary loop, we nest another for loop through each person's favorite language.
#Now this allows each person to list as many favorite languages as they like.

#You can refine the program even further. 
#You can include an if statement at the beginning of the dictionary's for loop.
#This way we can check if each person has more than one favorite language by examining of len(languages)
#If a person has more than one favorite language, the output would stay the same.
#If the person has has only one favorite language you could change the wording to reflect that.

#NOTE GUIDELINE 
#You SHOULD not nest list and dictionaries to deeply.
#If you're nesting items much deeper than a second or third nest or working with another persons code with significant levels of nesting,
#This likely indicates a simpler way to solve the problem. 

##################################
## A Dictionary in a Dictionary 
##################################

#In Python, you can nest a dictionary inside another. This however increases the complexity of your coding solution.
#Lets look at the example, if you have several users for a website, each with a unique username.
#You can use the usernames as the keys in a dictionary. 
#You then store information about each user by using a dictionary as the value associated with their username.
#In the following listing, we will store three pieces of information about each user.
#The user's first name, last name, and location. 
#we will be accesssing the information by looping through the usernames and the dictionary for infriomation associate with said username.

users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
    },
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

#In the example above, we first define a dictionary called users with two keys.
#One for each usernames with were 'aeinstein' and 'mcurie'.
#The value associated with with each key is another dictionary.
#This dictionary stores the user's first name, last names and location.
#We use each key to generate a neatly formatted full name, and location of each person. 

#We use a for loop to go through the user's dictionary. Python stores each key in the temp variable username.
#The dictionary associated with each username value goes into the variable user_info. 
#We can then access the nested dictionary. This has the information about users first name, last name, and location.

#We use each key to generate a formatted full name and location for each person.
#Then the program print the summary about each user.
#Notice that the instructions of each dictionary is identical. 
#Altough Python does not require identical formatted dictionaries, same structure makes it easier to work with nested dictionaries.

########################################
## TRY IT YOURSELF EXERCISES DICTIONARY
########################################
print("\n")
#People Exercise 
#Star with the program in the previous set of exercises.
#Start with making two new dictionaries with two keys for two different new people.
#And store all three dictionaries in a list called people.
#Then loop through your list of people. As your loop through the list, print every piece of information about that person.

Person1 = {
    'first_name' : 'Junjie',
    'last_name' : 'Li',
    'age' : '33',
    'city' : 'Trenton',
}

Person2 = {
    'first_name' : 'Vamshi',
    'last_name' : 'Bal',
    'age' : '32',
    'city' : 'Richmond',
} 

Person3 = {
    'first_name' : 'Rayon',
    'last_name' : 'Lore',
    'age' : '54',
    'city' : 'Fairbanks',
} 

people = [Person1, Person2, Person3]

for person in people:
    print("The person's name is " + person['first_name'] + " " +
    person['last_name'] + " and their age is " + person['age'] +
    " years old, and they live in " + person['city'] + ".")

#Pets Exercise
#Now make several dictionaries, where the name of each dictionary is the name of a pet.
#For each dictionary, include the kind of animal and owner's name.
#Store these dictionaries in a list called pests. 
#Loop through the list and print everything you know about each pet.
print("\n")

Pet1 = {
    'pet_name':'Charles',
    'species':'Tiger',
    'owner_name':'Lacy'
}
Pet2 = {
    'pet_name':'Bob',
    'species':'Cat',
    'owner_name':'Builder'    
}
Pet3 = {
    'pet_name':'Melody',
    'species':'Tarantula',
    'owner_name':'Cara'
}

pets = [Pet1,Pet2,Pet3]

for pet in pets:
    print("The pet's name is " + pet['pet_name'] + 
    ", and they are a " + pet['species'] + " and they're owner is " +
    pet['owner_name'] + ".")

#Favorite Places Exercise
#Make a dictionary called favorite_places.
#Think of three names to use as keys in the dictionary. 
#Store one to three favorite places for each person. 
#Loop through the dictionary and print each person's name and their favorite places. 

favorite_places = {
    'Junjie': ['Fuzhou' , 'New_York', 'Jersey_City'], 
    'Vamshi': ['San_Francisco','Libya','London'],
    'Josh'  : ['Houston','Cancun','Belize']  
}

for name, places in favorite_places.items():
    print("\n" + name.title() + "'s three favorite places are:")
    for place in places:
        print(place.title())

#Modify the program from exercise Favorite Numbers
#Make it so that each person can have more than one favorite number.
#Then print each person's name and their favorite numbers.

#Favorite_Numbers = {
#    'Logan'  : 'twelve' ,
#    'Paul' : 'hundred' ,
#    'Dan' : 'one' ,
#    'Josh' : 'fifty' ,
#    'Loco' : 'nine' ,
#}

Favorite_numbers_list = {
    'Logan': [100,18,171,2000],
    'Paul':  [100,18,171,2000],
    'Dan':   [100,18,171,2000],
    'Josh':  [100,18,171,2000],
    'Loco':  [100,18,171,2000],
}

for name, number in Favorite_numbers_list.items():
    print("\n" + name.title() + "'s favorite numbers are:")
    for num in number:
        print(str(num))

#Cities Exercise
#Make a dictionary called cities. Use the names of three cities as keys in your dictionary.
#Create a dictionary of information about each city, and include the country of origin. 
#,its approximate population, and one face about that city.
#The keys for each city's dictionary have values for country, population, and fact.
#Print the name of each city and all of the information you have stored about it. 
#Print the name of each city all of the information about that city.

cities = {
    'Shanghai' : {
        'country':'China',
        'population':'34,000,000',
        'fact': "The city's name literally means Upon the Sea in chinese."
    },
    'New_York_City' : {
        'country':'United_States',
        'population':'8,175,133',
        'fact': "The city had a record of 62.8 million tourists visit in 2017."
    },
    'Abu_Dhabi' : {
        'country':'United_Arab_Emirates',
        'population':'1,450,000',
        'fact':"Abu Dhabi holds about 9'%' of the worlds oil reserves."
    }
}

for city, info in cities.items():
    country = info['country']
    population = info['population']
    fact = info['fact']
    print("\nThe city of " + city.title() + " is located in the country of " + country.title() + 
    " and has a population of " + population + " people. One fact about " + city.title() + 
    " is, " + fact)


#Extensions Exercise
###########################################
#Use one of the example programs from the chapter and extend it by adding new keys and values, 
#changing the context of program and improving the format of the output. 
#I will however, make a new program called automobili, which is italian word for cars.
#This will be from an extension of an earlier dictionary in the beginning of the chapter called autobook.
#It will have the name of car is the key and have a another dictionary as the value pair with information,
#about the manufacturer, price, and body style. 

automobili = {
    'Focus_ST':      {'manufacturer':'Ford','price':'$25,170','body_style':'hatchback'},                   
    'Model_X':       {'manufacturer':'Tesla','price':'$81,000','body_style':'SUV'},           
    'Veyron':        {'manufacturer':'Bugatti','price':'$1,700,000','body_style':'coupe'},            
    '675LT':         {'manufacturer':'','price':'$335,566','body_style':'coupe'},         
    'Crown_Victoria':{'manufacturer':'','price':'','body_style':'sedan'}
}

for car, facts in automobili.items():
    print("\nInformation about the " + car.title() + ":")
    for detail, info in facts.items():
        print(detail.title() + " is, " + info.title())

#####
#End
#####

