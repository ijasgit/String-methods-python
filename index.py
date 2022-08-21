# String methods.....
# 1.capitalize()
#In the example below, capitalize() method is used to convert first character of the string called MyString into uppercase and rest into lowercase. This method does not change the MyString and only returns the converted version of it.
print("1.capitalize()")
word = "name"
print(word.capitalize())


#2.casefold()
#It is similar to string lower() method but stronger version, which converts more characters into lowercase. Due to this feature, it finds more matches when comparing two strings after converted using casefold() method
print("2.casefold()")
word2 = "NAme"
print(word2.casefold())

#3.center(length,"character")
#In the example below, center() method is to return the string with specified length and padded from left and right. If the specified length is less than the length of the string, no padding is done
print("3.center()")
word2 = "NAme"
print(word2.center(11,"/"))

#4.count(value,start,end)
#Note:This is method case sensitive while finding value
#In the example below, count() method is used to count number of occurrence of a specified character(s) in the given section of the string
print("4.count()")
word2 = "what is your Name"
print(word2.count("a",2,15))

#5.endswith(value,start,end)
#Note:This is method case sensitive while finding value.
#The Python endswith() method is used to check whether the string ends with specified value or not. It returns true when the string ends with the specified value, else returns false.
print("5.endswith()")
word2 = "what is your Name"
print(word2.endswith("me",2,20))

#6.expandtabs(tabsize)
#Note:Use \t for spacing.
#The Python expandtabs() method is used to set the tab size within the specified string. This method has one optional parameter which is used to specify the tab size. Default value of tab size is 8 whitespaces.
print("6.expandtabs()")
word2 = "w\th\tat isyourName"
print(word2.expandtabs(),"\n")

#7.find(value,start,end)
#The Python find() method is used to find out the index number for first occurrence of specified character(s) in the given string. This method is very similar to index() method. Only difference is that index() method which gives exception error.
# when character(s) is not found in the string and find() returns -1.
print("7.find()")
word2 = "what is your Name"
print(word2.find("me",2,20))

#8.format(values1,values2...)
#Note:Their are different types of formatting. 
#The Python format() method returns the formatted version of the given string where the specified values are inserted into the string's placeholder. The placeholder is defined using curly brackets: {}.
print("8.format()")

#default arguments
MyString = "I am {} and I am {} years old."
print(MyString.format("John", 25))

#positional arguments
MyString = "I am {0} and I am {1} years old."
print(MyString.format("Kim", 29))

#keyword arguments
MyString = "I am {name} and I am {age} years old."
print(MyString.format(name="Marry", age=22))

#mixed arguments
MyString = "I am {0} and I am {age} years old."
print(MyString.format("Sam", age=28))

print("Types of formatting")
#using decimal integer format
MyString = "Hello {}, your balance is {}."
print(MyString.format("John", 1000.23))

#using binary and hexadecimal format
MyString = "25 in binary format is {:b}, and in hexadecimal format is {:x}."
print(MyString.format(25, 25))

#using right align format
MyString = "{:>5}"
print(MyString.format(25))

#using padding for float number
MyString = "{:.2f}"
print(MyString.format(25.125125))

#9.format_map(mapping)
#The Python format_map() method returns the formatted version of the given string where the specified values (provided from mapping) are inserted into the string's placeholder. The placeholder is defined using curly brackets: {}
print("9.format_map()")
MyString = "I am {name} and I am {age} years old."
word2 = {'name':'ijas',"age":"23"}
print(MyString.format_map(word2))

mapping = {'name': ['John', 'Marry'], 'age': [25, 22]}

MyString = "I am {name[0]} and I am {age[0]} years old."
print(MyString.format_map(mapping))
MyString = "I am {name[1]} and I am {age[1]} years old."
print(MyString.format_map(mapping))

#10.index(value,start,end)
#The Python find() method is used to find out the index number for first occurrence of specified character(s) in the given string. This method is very similar to index() method. Only difference is that index() method which gives exception error.
# The index() method raises exception when the specified character(s) is not present in the string..
print("10.index()")
word2 = "what is your Name"
print(word2.index("me",2,20))

#11.isalnum()
#Note:Even space is present it return false. 
#The Python isalnum() method is used to check whether all characters of the string are alphanumeric or not. It returns true when all characters of the string is alphanumeric, else returns false. Alphanumeric characters belongs to numbers 0 - 9, letters A - Z (both uppercase and lowercase)
print("11.isalnum()")
word = "what1isyourName"
print(word.isalnum())

#12.isalpha()
#Note:Even space is present it return false. 
#The Python isalpha() method is used to check whether all characters of the string are alphabets or not. It returns true when all characters of the string is alphabets, else returns false. Alphabet characters belongs to letters A - Z (both uppercase and lowercase)
print("12.isalpha()")
word = "what1isyourName"
print(word.isalpha())

#13.isdecimal()
#Note:Decimal characters belongs to numbers 0 - 9.
#Note:Even space is present it return false. 
#The Python isdecimal() method is used to check whether all characters of the string are decimal or not. It returns true when all characters of the string are decimal, else returns false.
print("13.isdecimal()")
word = "1232"
print(word.isdecimal())

#14.join()
#Note:While using object in join() methold,key value are joined.
#The Python join() method returns a string which contains all elements of an iterable separated by the specified character(s). For this method, all elements of the iterable must be string.
print("14.join()")
joinBy="-"
word = ["i","am","from","chennai"]
MyDict = {
   "name": "John",
   "age": 25,
   "city": "London"
}
print(joinBy.join(word))
print(joinBy.join(MyDict))

#15.Lower
#The Python lower() method is used to convert all characters of the string in lowercase. Any symbol, space, or number in the string is ignored while applying this method. Only alphabet are converted.
print("15.lower()")
word = "HeLLO WorLD"
print(word.lower())














 