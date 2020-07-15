# Use {} for dictionary defination
# Dictionary use key and value pair for elements

practiceDictionary = {1:"python" , 2:"java" , 3:"android" , 4:"spring boot"}

print(practiceDictionary) # Printing values

print(practiceDictionary[1]) # Print the value with the given key

print(practiceDictionary.get(10 , "not found")) # if given key is not available then , it will print string mentioned.

practiceDictionary[10] = "php" # Adding new key value to the dictionary

print(practiceDictionary) # Printing dictionary