# Exceptions are Runtime Errors

a = 5
b = 2

try:
    print(a/b)  # Statement to check
except Exception as e:  # it will execute only when try statement has an error.
    print("Hey! check your values : " , e)

finally: # finnaly will execute always if we will get the exception or not.
    print("Working")