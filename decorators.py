def exception_catcher(func):
    def inner(*args): #1         
            try:
                    return func(*args) #2
            except Exception as ex:
                    print('unable to execute: ' + type(ex).__name__  + ' raised' )
    return inner

def unwrapped_divide(n, d):
    quotient = n/d
    return quotient

wrapped_divide = exception_catcher(unwrapped_divide)  #3

wrapped_divide(2, 0)
#unable to execute: ZeroDivisionError raised



# Let's first look at what's happening on a high-level and then dive into the details
# exception_catcher is a simple function decorator that takes any function, func and
# returns a wrapped function. This wrapped function will attempt to execute func and if 
# an exception is raised, it will log the exception in the console.


@exception_catcher      # divider = exception_catcher(divider) 
def divider(n, d):      # would acheive the same effect as @ 
    quotient = n/d
    return quotient

@exception_catcher
def filereader(filename):
    with open(filename) as file:
        return file.read()

filereader('nonexistent_file.txt')
#unable to execute: FileNotFoundError raised



# so what's going on with exception_catcher ?
# exception_catcher returns a callable, specifically the nested function inner.
# if we look at the line marked #3, we can see that the wrapped_divide now refers
# to a callable that can be called multiple times.
# Note that use of @func_decorator above def func(a,b,c...) -- as seen on the line
# marked #4 -- is 'equivalent' to wrapped_func = func_decorator(func)
 

# The callable returned by exception_catcher will have different properties, depending
# on what func was passed to exception_catcher. Notably, the variable func (#2) may be
# different for different calls to exception_catcher(func). You may be wondering
# how wrapped_divide(arg1, arg2) accesses func. By the time inner executes, exception_catcher 
# has finished executing and -- as func is a param of exception_catcher -- the reference to
# func should no longer exist, right? However, python supports a functional programming technique 
# called closures. This means nested functions maintain references to variables in their outer 
# function's namespace, after the outer function has finished executing.

# Lastly you may be wondering what the *args syntax on the lines marked #1 and #2 refers to.
# I won't get into the details here but suffice it to say, the use of * allows inner and func
# to accept arbitrary numbers of positional arguments. To find out more about the * operator
# check out:    https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists
# and   http://stackoverflow.com/questions/2921847/what-does-the-star-operator-mean-in-python/2921893#2921893
                          



