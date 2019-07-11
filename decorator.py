
def addAttributes(func):
    def sayHello():
        print("hello world")
    def newFunc(*args, **kwargs):
        sayHello()
        return func(*args, **kwargs)+12
    return newFunc

@addAttributes
def func(x,y):
    return x+y

print(func(12,3))
