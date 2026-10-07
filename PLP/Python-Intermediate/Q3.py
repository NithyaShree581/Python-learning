""" Topic: Decorators & Context Managers 
Implement the following two Python patterns: 
(a) Decorator @log_call: prints 'Calling <name>...' before and 'Done.' after. Apply to sum_to_n(n). 
(b) Decorator @retry(times=3): re-calls function up to 3 times on Exception. Simulate random failure. 
(c) Custom context manager TempFile: creates file on __enter__, deletes on __exit__. Write and read 3 lines. 
(d) Predict the output: def double(func):     def wrapper(x):         return func(x) * 2     return wrapper @double def square(n): return n * n print(square(3)) print(square(5)) 
 """
#(a)
def log_call(func):
    def wrapper(n):
        print("before")
        func(n)
        print("after")
        

    return wrapper
@log_call
def something(n):
    totalsum=0
    for i in range(1,n+1):
        totalsum=totalsum+i
    print(totalsum)
n=int(input("enter the numbers"))
something(n) 
#b

import random

def random_call(func):
    def wrapper():
        print("before")
        for i in range(1, 4):
            try:
                print("Attempt no is", i)
                if random.random() < 0.5:
                    raise Exception("Random failure")
                func()
                print("Success!")
                break
            except Exception as e:
                print(f"Failed at: {e}")
        print("after")
    return wrapper
@random_call
def random_calls():
    print("Function executed successfully")
random_calls()  
