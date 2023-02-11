# a function named arb_args that takes in any number of arguments and prints them one at a time
print("function 1")

def arb_args(*argument):
    for x in argument:
        print(x)

arb_args(24, "hello", (22))

# a function named inner_func that takes in two integers, two nested functions should perform seperately.  Distinct math operations using the integers.
print("function 2")

def inner_func(a, b):
    def func1():
        return a+b
    def func2():
        return b-a
    print(func1()+func2())

inner_func(5, 20)

