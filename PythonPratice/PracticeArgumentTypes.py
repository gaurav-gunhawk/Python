def check(a , *b): # *b can accept n no. of arguments as a tuple format.
    print(a , end =" ")
    print(b)

def check2(a , **b): # **b can accept n no. of arguments as a dictionary format as key,value pair.
    print(a , end =" ")
    print(b)


check(21 , 'gaurav',7,'python')
check2(21 , name="guarav", rollno=7 , language="python")
