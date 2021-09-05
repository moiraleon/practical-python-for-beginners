# age = input("How old are you?\n")
age = int (input("How old are you?\n")) #wrapping function in int
decades = age//10 # two // is whole number division
years = age % 10 #modulus finds remainder
# print ("You are " + decades + " decades old.") #cant concatenate floats so convert to string
print ("You are " + str(decades) + " decades old and " + str(years) + " years old")