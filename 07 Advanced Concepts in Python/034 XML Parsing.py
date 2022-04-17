from xml.dom.minidom import parse
import xml.dom.minidom

def Hello (str):
    "This function will print a Hello + the string provided"
    print("Hello "+str)
    return

def changeit (mylist):
    "We will change the passed list into this function"
    mylist.append([1,5,10,15])
    print("Values inside the function: ", mylist)
    return

def sum(num1, num2):
    " Add 2 numbers and return the sum"
    total = num1 + num2
    print("The sum is: ", total)
    return total
    

print ("HELLO PYTHON - HELLO WORLD - HELLO STUDENTS!")

counter = 100    # An integer variable is declared
message = "HELLO WORLD"  # A string variable
a, b, c = counter, counter,message # I assign the value of the variable counter and the value of the variable message to the variables a,b and c

print(a)
print(b)
print(c)
print(message)

# D A T A  T Y P E S  O F  P Y T H O N
# 1. Numbers
# 2. String
# 3. List
# 4. Tuple
# 5. Dictionary

var1 = 2000 # 1. Number
del var1 # We delete the reference to the number object var1

# Numeric Types
# A. int  (Integers)
# B. float (floating point real values)
# C. long (long integers)
# D. complex (complex numbers)


# S T R I N G
str = "How are you?" #String variable
print(str)
print(str[0]) #Print the first character of the string
print(str[2:7]) # Print characters starting from the 3rd to the 7th character
print(str+ "... HELLO PEOPLE!") # Print concatenated strings
print(str*4)  # Print string 4 times


# L I S T S
list = ['Hello world', 150, 1.25, 'My name is Christos', 100.25]
tinylist = [300, 'Christos']

list[2] = 500
print('--- L I S T S ---')
print(list)   # Print the complete list
print(tinylist*2)  # Print the tinylist 2 times
print(list[0])  # Print the first element of the list
print(list[1:3])  # Print the second till third element of the list
print (list+tinylist)


# T U P L E S
sample_tuple = ('Hello Christos', 185, 3.14, 'Hi again', 150.23)
tiny_sample_tuple = (450, 'Christos')
print('--- T U P L E S ---')
print(sample_tuple)   # Print the complete sample_tuple
print(tiny_sample_tuple*2)  # Print the tiny_sample_tuple 2 times
print(sample_tuple[0])  # Print the first element of the sample_tuple
# Print the second till third element of the sample_tuple
print(sample_tuple[1:3])
print (sample_tuple+tiny_sample_tuple)


# D I C T I O N A R I E S
dictionary = {}
dictionary['one'] = "This is the 1st element"
dictionary[2] = "This is the 2nd element"

tiny_dictionary = {'name': 'Christos', 'age': '33',
                   'id': '23456', 'job': 'instructor'}

print('--- D I C T I O N A R I E S ---')
print(dictionary['one'])  # Print the value of key 'one'
print(dictionary[2])      # Print the value of key 2
print(tiny_dictionary)    # Print the complete tiny_dictionary
print(tiny_dictionary.keys())  # Print all the keys
print(tiny_dictionary.values())  # Print all the values


# SINGLE IF STATEMENTS
print('--- I F   S T A T E M E N T S ---')
var1 = 5000
if (var1 == 5000):
    print ("The value of the variable is 5000")
print("This is the 2nd command")


# IF - ELSE  STATEMENTS
print('--- I F  E L S E    S T A T E M E N T S ---')
var1 = 5000
if (var1 == 5000):
    print ("The value of the variable is 5000")
else:
    print ("This is the 2nd command")


# IF - ELIF - ELSE  STATEMENTS
print('--- I F   E L I F   E L S E    S T A T E M E N T S ---')
var1 = 3000
if (var1 == 3000):
    print ("The value of the variable is 3000")
    print ('*********************************')
elif (var1 == 4000):
    print ("The value of the variable is 4000")
    print ('*********************************')
elif (var1 == 5000):
    print ("The value of the variable is 5000")
    print ('*********************************')
else:
    print ("The value of the variable is not 3000, 4000, 5000")


# NESTED IF STAMENTS
var1 = 3000
if (var1 == 1000):
    var2 = 4000
    if (var2 == 2000):
        print('Var2 is 4000')
    else:
        print('Var2 is not 4000')


# L O O P S

# 1st Loop Example: WHILE
print('--- W H I L E  L O O P ---')

i = 0
while (i < 5):
    print('The value of i is ', i)
    i = i + 1
else:
    print ('The value of i is equal or more than 5, it is ', i)
print('End of program.')

# 2nd Loop Example: FOR
names = ['Christos', 'Maria', 'John']
for name in names:
    print('Current name :', name)
print("End of program.")

# 3rd Loop Example: FOR
print('--- F O R  L O O P ---')
i = 0
for i in range(0, 5):
    print('The value of i is ', i)
    i = i + 1
else:
    print ('The value of i is equal or more than 5, it is ', i)
print('End of program.')

# 4th Nested While Example Loop
print('--- N E S T E D  W H I L E  L O O P ---')

i = 0
while (i < 5):
    j = 0
    while (j < i):
        print('The j value is', j)
        j = j + 1
    print('The value of i is ', i)
    i = i + 1
else:
    print ('The value of i is equal or more than 5, it is ', i)
print('End of program.')


mylist = [10, 20, 30]
changeit(mylist)
print("Values outside are now", mylist)
total = sum(10, 20)
print("I am printing again the sum of the two numbers is ...", total)
print(sum(450, 1203))

# F U N C T I O N S
# I will all the Hello to print a string
Hello("WORLD!")
Hello("to all of u!")

mylist = [10, 20, 30]
changeit(mylist)
print("Values outside are now", mylist)
total = sum(10, 20)
print("I am printing again the sum of the two numbers is ...", total)
print(sum(450, 1203))

# I N P U T  - O U T P U T
#READING DATA FROM KEYBOARD
str = input("Type something here with you keyboard: ")
print("You typed: ", str)

# WRITING DATA TO FILE
f = open("c:/myfile.txt", "w")
print("Name of file is", f.name)
print("It is ", f.closed)
print("It is ", f.mode)
f.write("HELLO BEAUTIFUL WORLD!")
f.close()

# READING DATA FROM FILE
f = open("c:/myfile.txt", "r")
str = f.read()
print (str)
f.close()


# I will all the Hello to print a string
Hello("WORLD!")
Hello("to all of u!")

mylist = [10, 20, 30]
changeit(mylist)
print("Values outside are now", mylist)
total = sum(10, 20)
print("I am printing again the sum of the two numbers is ...", total)
print(sum(450, 1203))


# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse("C:\\Users\\hp2560p\\Documents\\testxml.xml")
collection = DOMTree.documentElement

# Get all the movies in the collection
products = collection.getElementsByTagName("PRODUCT")

for product in products:
   print ("*****Product*****")
   if product.hasAttribute("ITEM"):
      print ("Title: %s" % product.getAttribute("ITEM"))
