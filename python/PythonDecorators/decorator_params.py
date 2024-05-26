def do_twice(func):
    def wrapper_do_twice(*args,**kwargs):
        func(*args,**kwargs)
        func(*args,**kwargs)
    return wrapper_do_twice

@do_twice
def hello():
    print("Hello")

@do_twice
def greet(msg):
    print("Hello " + msg)

hello()
greet("World")

def return_greetind(name):
    print("greeting function")
    return f"hello, {name}" 