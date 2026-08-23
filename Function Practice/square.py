#Passing function as Arguments

def fun(func,arg):
    return func(arg)
def square(x):
    return x**2
res = fun(square,5)
print(res)

#Using *args

def stat(*args):
    for arg in args:
        print(arg)
stat(1,2,3,4,5)