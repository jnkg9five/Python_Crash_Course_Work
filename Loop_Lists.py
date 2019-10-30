#Python_List_Exercise
#PYTHON CRASH COURSE Chapter#4 LISTS

#What is a List?
#List is a collection of elementss in a particular order. 
#You can put any data you want in a list.
#elementss in a list don't have to be categorically related. ex. Integers, Strings, Floatpoints
#In Python, a list is contains in square brackets. 

#########################################
# Looping through a List
#########################################

#You want to run through all entries in a list.
#You want to do the same operation with each element.

#We have a list and we want to get every element of the list printed. HOW TO?
cars = ['Zonda','Agera','Carrera_GT','Veyron']
for car in cars:
    print(cars)

#We just used a for loop to print all the elements in the list cars
#the for loop has a temporary variable that holds each value in the list for each rescursion. 
#Recursion is the method or concept of repeating the same call or function over and over again.
#Iteration is the method or concept of having a call or function repeated until a certain condition is met. 
#Recursion uses more memory and is slower on a computer machine. Less complex than iterative solutions.

#You can show the concept of recursion by printing multiple times with a for loop in Python
cars2 = ['ID_3','Model_3','Bolt','Leaf','Rimac_C2']
for car in cars2:
    print(car.title() + ", is my favorite car.")
#You can keep having recursion on every line within the for loop
    print(car.lower() + ", is my favorite car.")

#Use tab or space not both to indicate when the scope of your loop ends

print(car + "is my favorite car.") #notice how the last value of the temp variable is still maintained in memory.

#########################################
# Numerical Lists / Indentation Errors
#########################################

# Python uses indention (tab/spaces not mixed) to determine is lines of code are connected.
# The indentations in Python show the overall program's organization. 
# DO NOT MIX SPACES OR TABS. 

#You can use the range() function to generate a series of numbers.
for value in range(1,10):
    print(value)

#Now you can use the range() function is the list() function to create a list within the range parameters.
numbers = list(range(1,15))
print(numbers)

#The range function can take a third parameter to iterate by a value until list is complete
numbers = list(range(0,100,10))
print(numbers)

#Lets now combine several concepts of for loops, numerical lists, and operand for exponents **.
squares = []
for value in range(1,10):
    square = value**2
    squares.append(square) 

print(squares)

#The above function declared a list variable squares. Then uses a for loop to create a list with temp value var.
#The range function specifies the size of the list to be made. 
#The squared value is stored in temp var square and then append() to the squares list and finally printed.

#BUT you can make the code more concise.
square2 = []
for value in range(1,15):
    square2.append(value**2)

print(squares)

#There are some statistical functions you can apply to lists.
digits = range(2,10,2)
mini = min(digits)
maxi = max(digits)
total = sum(digits)

print("The min value of digits is " + str(mini) + ". The max value is " + str(maxi) + ". The total value is " + str(total) + ".")

#List Comprehensions can generate more complex logic for lists. 
#It combines the for loop and adds to new elements and appends them to the list in the same line.
squares = [value**2 for value in range(1,10)]
print(squares)

#########################################
# Numerical Lists Pratice Exercises
#########################################

#Use a for loop to print the numbers from 1 to 20 inclusive.
for numbers in range(1,21):
    print(numbers)

#Print the numbers one to one million, then use min() and max() to make sure your list starts at 1. Ends at 1 million.
one2onemil = range(1,1000**2+1)
mini = min(one2onemil)
maxi = max(one2onemil)
total = sum(one2onemil)

print(total)

#Make a list of the ODD NUMBERS, use the range() functions from 1 to 20, print each number.
oddnum = range(1,21,2)
for numbers in oddnum: #oddnum defines the list size in the for loop
    print(numbers)

#Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the list.
threethirty = range(3,31,3)
for numbers in threethirty:
    print(numbers)

#MAke a list of the first 10 cubes and use a for loop to print out the value of each cube.
thecubes = list(range(1,11)) #cannot perform operand on entire list all at once
cubes = []
for cube3 in range(0,10): 
    cubes.append(thecubes[cube3]**3) #You have to index from 0.

print(cubes)

#Use a list comprehension to egenerate a list of the first 10 cubes.
cubes22 = [value**3 for value in range(1,11)]
print(cubes22)

#########################################
# Partitioning/Slicing a List
#########################################

#You can slice a list to segment part of it to manipulate or change.
character = ['charles','martina','michael','florence','eli']
print(character[0:3]) #this will print [charles, martine, michael] index 0

#You can slice from the beginning of a list automatically 
print(character[:3]) #will print the same as above. 
#And you can slice from a specific index to the end of the list
print(character[3:])
#And don't forget that negative index number will rollback from the end of the list.
print(character[-3:])

#Slices are useful in for instance games. You can add a player's final score to a list every time a player finishes playing.
#You can get the top 3 scores by slicing the first three scores. So when working with data, you can use slices 

#So here is a list slice to show the top three characters.
print("Here are the top three characters in my book series: ")
for player in character[:3]:
    print(player.title())

#NOW you can go and copy a list. 
#Lets say you want to make a new list of an existing list you instantiated. 
#Lets make a list of favorite foods. Then copy that list to a list for my friends favorite food.
my_foods = ['pizza','falafel','carrot_cake']
friend_foods = my_foods[:] #using [:] copies the entire list

print("My favorite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are also: ")
print(friend_foods)

#There are TWO seperate lists. They are not linked lists. To demonstrate, we will append another element to one.
friend_foods.append('jackfruit')
print(friend_foods)
my_foods.append('mango')
print(my_foods)

#To set two different lists, you have to use slicing [:]

#########################################
# Partitioning/Slicing a List Exercises 
#########################################

#Using the programs add several lines to the end of the programs you written.
#Print the first three items in the lists.
print("The first three items in the list are: ") 
print(my_foods[:3])
#Print the three items from the middle of the list.
print("The items from the middle of the list are: ")
print(my_foods[2:4])
#Print the three items for the last three of the list.
print("The last three items in the list are: ")  
print(my_foods[-3:])

#########################################
# Tuples 
#########################################

#List work well for storing sets of elements. Sometimes you want a list that cannot change.
#You can use Tuples. Python has values that cannot change/immutable. 
#An immutable list is called a tuple. 

#Tuples look like a list except you use paretheses ().
dimension = (200, 50)
print(dimension[0]) #200
print(dimension[1]) #50
#dimension[0] = 250 This will not work, reassigning tuple value not allowed.

#To change tuple, you have to redefine the entire tuple list. 
dimension = (400, 100) #block defines the tuple.
print(dimension[0])
print(dimension[1]) #tuples are simple data structures. 
for dim in dimension: #You can use the for loop.
    print(dim)

#END/FINALE






