def logger(func):
    def wrapper():
        print("======logging start=======")
        func()
        print("======logging end  =======")
    return wrapper


@logger
def sample():
    return print("---------sample func---------------")


sample = sample()