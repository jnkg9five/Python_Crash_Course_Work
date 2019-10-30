#Python_List_Exercise
#PYTHON CRASH COURSE Chapter#3

#What is a List?
#List is a collection of elementss in a particular oder. 
#You can put any data you want in a list.
#elementss in a list don't have to be categorically related. ex. Integers, Strings, Floatpoints
#In Python, a list is contains in square brackets. 

#########################################
# Creating and Accessing a List
#########################################

#Lets make a list for cars

cars = ['Corvette','Beetle','Zonda','720s']
print(cars[0])
print(cars[1]) 
print(cars[2]) 
print(cars[3]) 
#print(cars[4]) this causes IndexError because lists in python are indexed [0]. 

#You can use string class methods to manipulate elementss in the list to output differently. 
cars2 = ['corvette','beetle','zonda','evora']
#Example of printing capitalization of elementss with title() class method
print(cars2[0].title())
print(cars2[1].title())
print(cars2[2].title())
print(cars2[3].title())

#Quick example showing of indexing of [0] not [1]
print(cars[1])
print(cars2[3])
#Python has a special syntax for accessing the last element of a list. Use the index [-1]
print(cars[-1])
#The same concept with index[-n] with -n being the element with n position from the end of the list.

#Elements from a list can be concatenated into a message
message = "My first car I brought was a " + cars2[1].title() + "."
print(message)

#You can change the value of the elements in a list at any time
#cars = ['Corvette','Beetle','Zonda','720s']
cars[0] = 'FordGT'
print(cars2)

#Lets now append things to the list
#I want to add another car to the list, how do I do that. 
cars.append('ID.3')
print(cars)
#We use the append() class method. 
#But you can also insert elements into a index position. 
cars.insert(0, 'Veyron')

#Lets say we want to remove an element from a list, how do we do That. 
#I do not like Fords, they're unreliable and made in Mexico. 
del cars[0]
print(cars)
#You can use the del method. It removes the index element from your list. 
#With this you cannot access the element that was removed anymore. ITS GONE!
#But you can also remove an element using the pop() class method
cars2.pop()
cars2.pop(1)
print(cars2)
#For the pop() class method, it removed the last element in the list, 
#BUT you can enter an integer parameter within the index of the list to pop out that particular element. 
#BUT you can also remove an item by value 
cars.remove('Zonda')
print(cars)

#Some do it yourself python exercises
#Make a list of 3 poeple you'll like to have breakfast with (living or dead).
guests_fd = ['Elon Musk','Isaac Newton','Richard Feynman']
print(guests_fd)
#BUT wait, Isaac Newton had an apple hit his head and sent him to hospital. 
#A new guest will be added to the list
guests_fd.pop(1)
guests_fd.insert(1, 'Tony Stark')
print(guests_fd)
#A wild Tony Stark has appeared and will be coming to breakfast

#########################################
# Organizing A List 
#########################################

#When lists are created they will most likely be unorganized. This may beyond your control or predicitions.
#You'll most likely want to organize your lists.
cars3 = ["audi","porsche","toyota","honda","pagani"]
cars3.sort()
print(cars3)
#The sort() class method arranges the elements in the list in alphabetical order
cars3.sort(reverse=True)
print(cars3)

#You can temporary sort a list with the sorted() function
print(cars3) #original list
print("\nThis is now the sorted list of cars3!")
print(sorted(cars3))
#Original list is unmodified 
print(cars3) # this is the same as original list

#Now printing a list in reverse order, you use argument reverse=True
print(cars2)
cars2.reverse()
print(cars2)

#You can find the length of a list using the len() function
Fibonnaci = ['1','1','2','3','5','8','13','21','34','55','89']
leng_fib = len(Fibonnaci)
print(leng_fib)
#Python counts elements in list starting at index 1.

#Lets do an exercise with list organization
#Make a list of 5 places in the world you'll like to visit.
#Store the locations in a list.
Destination = ['Miami','New_Zealand','Maui','Rome','Moscow']
#Print the list in order.
print(sorted(Destination))
#Use the sorted function to print in reverse alphabetical order
print(sorted(Destination, reverse=True))
#Show the list is still in original order
print(Destination)
#Reverse the list order
Destination.reverse()
print(Destination)
#Reverse the list order AGAIN
Destination.reverse() 
print(Destination)
#Use sort() to change list to store list in alphabetical order 
Destination.sort()
print(Destination)
#Use sort() to sotre list in reverse alphatical order
Destination.sort(reverse=True)
print(Destination)

#########################################
# Index Errors examples
#########################################

#Common error is forgetting about index [0]
#cars = ['1','2','3'] 
#print(cars[3]) 
#This will give an index error 
#Empty list index will give an error



