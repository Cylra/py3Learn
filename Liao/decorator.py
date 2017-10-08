#! /usr/bin/python3

def log(func):
    def wrapper(*args, **kw):
        print("call function (%s):" %(func.__name__))
        return func(*args, **kw)
    return wrapper

@log
def now():
    print("2017-08-20")

now()