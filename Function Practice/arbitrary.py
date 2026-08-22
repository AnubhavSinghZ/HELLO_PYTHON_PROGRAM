def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)
    print("Keyword Argument (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key}=={value}")
myFun('Hey', 'welcome', first='Geeks', mid='for', last='Geeks')

#  *args stores extra positional arguments.
#  **kwargs stores extra keyword arguments.
# loop prints all positional and keyword values separately