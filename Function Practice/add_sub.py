def add_sub(a,b):
    return(a+b,a-b)
a=100
b=30
add=add_sub(a,b)
sub=add_sub(a,b)
print(add, sub) #this will give the output like  (130, 70) (130, 70) (two times of the output)
