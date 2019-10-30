#Python_List_Exercise
#PYTHON CRASH COURSE Chapter#5
#IF STATEMENTS

#Programming in general involves examining a set of conditions. 
#Once certain conditions have been met the program will decide to execute parts of the program.
#If statements are a fundamental conditional statements in programming.

#Simple if statement with printing an element in a list.
cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title()) 

#The if statement in the for loop should only capitalize all the letters in bmw.

################################
# Conditional Tests 
################################

#Conditional statement can be evaluated as True or False. This is called a conditional test.
#If a conditional test evaluates to True, Python executes the code following the if statement. 
#If a conditional test evaluates to False, Python ignores the code following the if statement. 

#There is a different between an assignment operator = and the equality operator == .
#Quick conditional test.
car = 'bmw'
car == 'bmw' # Python interpreter will return a True 
car == 'audi' #Python interpreter will return a False

#Checking for Inequality
#When you want to see if 2 values are not equal, you can use the operator !=.
#Below is a conditional if statement with the not equal inequality operator.

requested_pizza = 'mushroom'

if requested_pizza != 'peppers':
    print("Wrong pizza man!")

#The conditional statement compares if the value of requested pizza holds mushroom. 
#It doesn't so it will print the statement in the if statement.

#Numerical Comparisions
age = 18 #you set age variable to hold value integer 18
age == 18 #you are checking the value to age and comparing if it equals 18. this will return True
#You can check to see if 2 numbers are not equal. 

#Lets check if age is set to value 42, which it is not.
if age != 42:
    print("That is not the correct value. Please try again!")

#Below are a continued list of common equality operators.
age = 19
age < 21
age <= 21
age > 21 #This will return False
age >= 21 #This also will be False

################################
# Checking Multiple Conditions
################################

#You may want to check multiple conditions at the same time.
#How do we do that? You want two specific conditions to be True to perform some process or execution.
#The keywords [and] and [or] can be used in these situations.

#To check if two conditions are both True at the same time, use the keyword [and].
account_value = 4000
stock_value = 200

account_value > 3000 and stock_value <= 200 #This will return value of True. 
#We are checking if account_value is greater than 3000 and checking if stock value is less than equal at the same time.

#To check if one of several conditions are True, use the keyword [or].
account_value < 3000 or stock_value <= 200 #This will return value of True.

################################
# Checking Conditions in Lists
################################

#Checking for value in a List

#You can check lists or conditions similar to the process of checking conditions for certain values.
#Lets say you have a list of usernames and passwords on a website, and you want to check if a username already exists.
#Then you want to compare a password against a certain lists of conditions before accepting a password.

#To find if a particular element/value is already in a list, use the keword [in]. 
#Lets reassign our stock_value to be a list of value (dollars)

stock_value = ['$400','$1000','$24','$3042','$2341','$3242']
'$3042' in stock_value #This will return value True
'$3000' in stock_value #This will return value False

#Checking for values NOT in a List

#Another conditions we want to check in a list is values not found in a list.
#For example, you want to see if a username was banned on a website. 
#We make a list of banned users.

banned_users = ['Bob','Burgers','Lisa']
user = 'marian'

if user not in banned_users:
    print(user.title() + ", you can continue to the secret page!")

#Boolean Expressions (True/False)
#A boolean expression is another conditional test.
#A boolean value is either (True/False 1/0).
#Boolean values are used to keep track of certain conditions, whether a game is running.
#If game is running then user cannot edit content

game_active = True
can_edit = False

#Boolean value are an efficient way to track a state of a program or particular condition.

################################
# Do it yourself questions
################################

#Write a series of conditional tests. Print a statement describing each test and your predicted result.
#Create at least 10 tests. 5 tests evalute to True and another 5 tests evaluate to False.

game_status = True
website_loading = False
battery = 80
phone = 'Iphone'
bread = ['Wheat','Rosemary']

if game_status is True:
    print("Continue playing")

if website_loading is False:
    print("Website is loaded!")

if battery < 100:
    print("Keeping charging your phone!")

if phone != 'Android': 
    print("Phone is Iphone!")

if 'Sourdough' not in bread:
    print("There is no Sourdough") 

age = 10
tires = 'michelin'
car = 'lamborghini'
local = 'Waco'
food = 'burger'

if age == 12:
    print(12)

print("Wrong age!")

if tires == 'continental':
    print("Right tires!")

print("Wrong tires!")

if car == 'camry':
    print("car better")

print("Car crashed!")

if local == 'Dallas':
    print('Your home!')

print("Your stranded.")

if food == 'fries':
    print("You are hungry")

print("You are a big " + food.upper())

################################
# If Statements
################################

#If statements can be used to allow programs to execute commands from the results of conditional tests.
#The basic if statements are simple if statements. You have condition and it will execute a command if True.

#if conditional_test:
    #do something

#Indentations have the same role in if statements as it did in for loops.
#All indented lines after an if statement will be executed if condition test is True.
#Make sure that indentions are proper. You can block with indentations.

age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote.")

################################
# If-Else Statements
################################

#In a conditional test, you want one action to execute on a condition and a different action in other cases.
#An if-else statement block is similar to a simple if statement, but the else statement allows to a an action to execute if condition fails.

#Example is shown below. 

cars2 = ['volkswagen','nissan','bugatti']
if cars2[0] == 'nissan':
    print("Your car is a nissan!")
else:
    print("I don't know the car you have!")

################################
# If-Elif_Else Chain
################################

#In many situations you'll need to test more than two possible conditions.
#You will use Python's if-elfif-else syntax. 
#Python executes only one block in an if-elif-else chain. 
#It runs these tests in sequence until one condition passes. Many real world situations involve more than two conditions. 

#Lets run through an example. An amusement park that charges rates for different age groups.
# Admission for anyone under age 4 is free.
# Admission for anyone between the ages of 4 and 18 is $5.
# Admission for anyone age 18 or older is $10.

#Set age to 12
age = 12

if age < 4:                       
    print("Go in for free!") #conditional test checks if age is less than 4
elif age < 18:
    print("Cost of admission is $5.") #conditional test checks if age is under 18
else: 
    print("You have to pay $10") #conditional test checks if age is greater than or equal to 18

#The elif statement evalutes as true so it will print Cost of admission is $5. 
#But there is another method to use. Rather than printing the admission price within each block,
#Set a variable to store the value of the price and use a simple print statement that runs after the chain is evaluated.

if age < 4:
    price = 0
elif age < 18:
    price = 5 
else:
    price = 10

print("Your admission cost is $" + str(price) + ".")

#The code produces the same type of result, but the chain is narrower. 
#Instead of checking condition and printing a message, it just stores the value of the price.
#This is more efficient and this code is easier to modify. If you need to change the output message , just change the print statement.

#Testing Multiple Conditions
#The if-elif-else chain is only good to use when you just need one test to pass. 
#However, if you want to check all conditions of interest. You will use a series of simple if statements.
#No elif or else blocks. This will be useful for problems where more than one condition can be true. 

#Simple Example with a pizza shop. 

requested_toppings = ['black_olives','mushrooms','jalapeno']

if 'black_olives' in requested_toppings:
    print("Adding black olives")
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
if 'jalapeno' in requested_toppings:
    print("Adding jalapeno")

print("\n Your pizza is finished.")

#The simple if statements above test multiple conditions to see if all the toppings are requested.
#It will print adding the topping and then print that the pizza is finished at the end.

#################################
#Try it Yourself Exercises
#################################

#Alien Colors #1: Imagine an alien was just shot down in a game.
#Make a variable called alien_color and assign it a vale of green, yellow, or red.

alien_color = 'green'

if alien_color == 'green':
    print("You earned 5 points.")

#Alien Colors #2: Write an if-else chain. If the alien's color isn't green, print a statement that the player earned 10 points.

else:
    print("You earned 10 points.")

#Alien Colors #3: Turn your if-else chain into a if-elif-else chain.
#If alien is green, print player earned 5 points.
#If alien is yellow, print player earned 10 points.
#If alien is red, print player earned 15 points.

#alien_color = 'green'
#alien_color = 'yellow'
alien_color = 'red'

if alien_color == 'green':
    print("You earned 5 points.")

elif alien_color == 'yellow':
    print("You earned 10 points.")

else:
    print("You earned 15 points.")

#Stages of Life: Write an if-elif-else chain to determine if a person's stage of life.
#If the person is less than 2 years old, print your a baby.
#If the person is at least 2 years old but less than 4, print your a toddler.
#If the person is at least 4 years old but less than 13, print your a kid.
#If the person is at least 13 years old but less than 20, print your a teenager.
#If the person is at least 20 years old but less than 64, print your an adult.
#If the person is age 65 or older, print your an elder.

age = 24
age = 13

if age < 2:
    print("Your a baby!")

elif age >= 2 and age < 4: 
    print("Your a toddler.")

elif age >=4 and age < 13:
    print("Your a kid.")

elif age >=13 and age < 20:
    print("Your a teenager.")

elif age >=20 and age <65:
    print("Your a adult.")

else:
    print("Your a elder.")

#Using if Statements with Lists
#Combining lists and if statements can allow you to watch for special values that need to be treated differently.
#For example, you can manage the avaliability of certain items in a restaurant through a shift.
#You can also begin to prove that your code works as expected in all possible situations. 

#Lets take a pizzeria example. What if a pizzeria runs out of green peppers.
toppings = ['mushrooms','green peppers','extra cheese']
    
for wanted_toppings in toppings:
    if wanted_toppings == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + str(toppings) + ".")

print("\nFinished making your pizza!")

#The program above checks to see if a person requested green peppers on their pizza.
#The condition tests checks for the green peppers and the the else statement ensures that other toppings will be added.

#####################################
## Checking That a List is not Empty 
#####################################

#A simple assumption about every list so far can be made, there at least is one element in it.
#We can let usesrs provide the information that's sotred in a list.
#It can't be assumed that the list has any elements each time a loop is run. Basically empty list.
#We can check for example if the list fo toppings is empty before making a pizza.

#If the list is empty, we can prompt the user and make sure they want a plain pizza.
#If the list is not empty, we use the program in with a non-empty list.

topping = []

if topping:
    for wanted_topping in topping:
        print("Adding " + wanted_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Do you really want a plain pizza?")

#The if conditional test above checks if the list topping is not empty.
#Then the for loop will check each (topping) element in the non-empty list and prompt the user that each (topping) element is added. 
#If the list is empty, it will prompt the user if they want just a plain pizza with no toppings.
#The program structure above is good for checking an empty list and how to handle cases for empty and non-empty lists.

#Using Multiple Lists.
#People will ask about anything. What if a customer requests a unusual topping request. 
#The follwing example defines two lists.
#The first is a list of avaliable toppings on the pizzas and second is a user requests. 

avaliable_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']

wanted_toppings = ['mushrooms','french fries','extra cheese'] #french fries are not avaliable

for wanted_topping in wanted_toppings:
    if wanted_topping in avaliable_toppings:
        print("Adding " + wanted_topping + ".")
    else:
            print("Sorry, we don't have " + wanted_topping + ".")

print("\nFinished making your pizza!")

###################################
## If Statement Exercises 
###################################

#Hello Admin
#Make a list of 5 or more usernames, include the name admin. 
#If the username is admin print a special message.
#Otherwise, print a generic greeting.

users = ['Eric','Sam','Rachel','admin','Laurel']
for logins in users:
    if logins == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + logins + ", thank you for login in again.")

#No Users
#Make sure the list the list of users is not empty 
#Remove all usersnames are removed form the lit and make sure the correct message is printed.
#We need to find some users!

users = []
if users:
    for logins in users:
        if logins == 'admin':
            print("Hello admin, would you like to see a status report?")
        print("Hello " + logins + ", thank you for logining in again.")
else: 
    print("We need to find some users!")

#Checking Usernames
#Do the following to create a program that simulates how a websites checks everyone has a unique username.
#Make a list of 5 or more usernames called current_users.

current_users = ['Hello','World','If','Else','Statements']

#Make another list of 5 usernames called new_users. Make sure two of the names are in present in current users.

new_users = ['Loco','Sparta','If','Hello','Manny']

#Loop through the new_users list to see if each new username has balready been used. 
#If it has, print a message that the person will need to enter a new username.
#If a username has not been used, print a message saying that the username is available. 
#Make sure your comparision is case insensitive. "John" is equal to "JOHN"
current_upper = []

for upper in current_users:
    current_upper.append(upper.upper())

for usernamer in new_users:

    if usernamer.upper() in current_upper:
        print("Username is taken, try another username.")
    else: 
        print("The username is avaliable.")

#Ordinal Numbers indicate their position on a list, such as 1st and 2nd. 
#Most ordinal numbers end in th, except 1, 2, and 3. 

th_list = [1,2,3,4,5,6,7,8,9]

for nth in th_list:
    if nth == 1:
        print("\n1st")
    elif nth == 2:
        print("\n2nd")
    elif nth == 3:
        print("\n3rd")
    else: 
        print("\n" + str(nth) + "th")