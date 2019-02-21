from inspect import getgeneratorstate
def simple_coroutine():
    print("-> started")
    x = yield
    print("-> end",x)

if __name__ == "__main__":
    my_cor = simple_coroutine()
    print(getgeneratorstate(my_cor))
    next(my_cor)
    print(getgeneratorstate(my_cor))
    my_cor.send(13)
    print(getgeneratorstate(my_cor))
    next(my_cor)
