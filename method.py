# using capitalize method 
txt = "hello, and Welcome to my world"
print(txt.capitalize())
#what if first character is number 
txt1="36 is my age"
print(txt.capitalize())
#Nothing changes

#using casefold()
print(txt.casefold())
# all the string move to lower case

#using center method
a='banana'
print(a.center(25))
#it generally centeralize the string 

#using count() method
b= "I am nitesh.currently, I am learning Python language.Python is most usefull language"
print(b.count("I"),b.count("balen"))
# Return the number of times the value "word" appears in the string

# using endswith() method
c="hello, my name is Nitesh."
print(c.endswith("esh."))
# it check the string with esh. or not...
c="hello, my name is hello"
print(c.endswith(("esh.","hello")))
# ends with esh. or hello ,if one it it then it print true


