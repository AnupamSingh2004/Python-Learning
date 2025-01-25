# Python is a General Purpose Programming Language
# Has a Large standard Library

print('Hello, Python!') 

import sys 
print(sys.version)

# type() shows us the data type of the input

print(type(12))

# Type Casting
print(float(10))
print(int(10.5))

# Type casting the int inside the string gives out the int inside the string unlike c++ in which we had to subtract '0' to get the actual int inside the string
print(int('10'))

# The code below gives an error 
# print(int('A'))


# int and float can be converted into Strings

print(str(20.5))

# In boolean Values it Is necessary to use Uppercase T and F in True and False
# int Value of 1 is True and of 0 is False and vice-versa

# this ->  // is used for Int division ,It rounds up the result

# Strings

# A string can be contained in single:' ' or double:" " quotes
# A string can be spaces or digits or special characters
# Its indexing is similar to C++ and starts with 0 bit Python has -ve indexing in which -1 is dedicated to the last character and 
# as we proceed to the beginning of the string the -ve value increases

# We can bind a String to another variable
name = "Anupam Singh"
short_name = name[0:4];

print(short_name)

# We can also use Striding and wwe can use it along with slicing 

print(name[::2])
print(name[0:5:2])

len(name) #Used to get the length of the string as in this case there are 12 elements so the length will be given as 12

# We can combine Strings

first_name = "Anupam"
print(first_name + " Singh")

# We can replicate the number of times the String by multiplying the string with an integer 

print(3 * first_name )

# strings are immutable which means the value cannot be changed but a new string can be created

Name = "Anupam "
Name = Name + "Singh"
print(Name)





