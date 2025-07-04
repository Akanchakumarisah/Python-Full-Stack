# def my_deco(func):
#     def wrapper():
#         print("something is happening before function")
#         func()
#         print("something is happening after function")
#     return wrapper
# @my_deco
# def say_hello():
#     print("Hello!")
# say_hello()
#Time series

import time

def calculateTime(func):
    def wrapper(*agrs,**kwargs):
        st = time.time()
        func(*args,**kwargs)
        end=time.time()
        return end-st
    return wrapper
@calculateTime
def greet(x):
    print(f"Hello Class! {x}")
    
func_val=greet("34-502")
print(f"function execution time is,{func_val}")