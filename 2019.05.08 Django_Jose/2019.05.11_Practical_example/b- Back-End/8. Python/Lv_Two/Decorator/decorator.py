def new_decorator(func):

    def wrap_func():
        print("CODE HER BEFORE EXECUTING FUNC")
        func()
        print(" FUNC() HAS BEEN CALLED ")

    return wrap_func

def func_need_decorator():
    print("THIS FUNCTIONG IS IN NEED OF DECORATOR")

# func_need_decorator = new_decorator(func_need_decorator)
#


#The above commented block of code is equivalent to this below:

@new_decorator()
def func_need_decorator():
    print("THIS FUNCTIONG IS IN NEED OF DECORATOR")

func_need_decorator()
