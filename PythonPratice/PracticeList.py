# We can add hetrogeneous elements in the list.
# Elements are in the sequential form as inserted in the list.
# Use [] for list defination.

practiceList = [1,'Welcome','to','the','practice','session']

practiceList.append(9) # Attach elements at last
practiceList.insert(1,34) # Attach elements at the given index
practiceList.extend([56,67,87]) # To add multiple elements in the list

print(practiceList)

practiceList.remove(87) # Remove the given element from the list
practiceList.pop() # Remove the last element from the list

print(practiceList)
