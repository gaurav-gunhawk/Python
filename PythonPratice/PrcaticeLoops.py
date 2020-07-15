# For loop
for i in range(0,5): # i value varies from 0 to 4
    print("Welcome")

# While loop
i=0
j=5
while i<j :
    print("Hello")
    i+= 1

# For else (Loop only present in python language)
numbers = [12,34,56,67,78]
for i in numbers:
    if i%5 == 0:
        print(i)
else:
    print("No element found")