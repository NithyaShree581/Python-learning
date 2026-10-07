"""Topic: Generators & Iterators 
Implement the following generator-based solutions: 
(a) fibonacci_gen() that yields Fibonacci numbers indefinitely (no list, no recursion). 
(b) take(n, gen) returning the first n values from any generator as a list. 
(c) squares_gen(limit) yielding squares of integers up to limit. 
(d) Use both generators to print the first 10 Fibonacci numbers that are also perfect squares. 
(e) Predict the output: def countdown(n):     while n > 0:         yield n         n -= 1 gen = countdown(5) print(next(gen)) print(next(gen)) print(list(gen)) 
"""
import math 
#a
def generator():
    a=0
    b=1
    while True:
        yield a
        
        a,b=b,a+b   
#b  take(n, gen) returning the first n values from any generator as a list. 
def take(n,gen):
    listt=[]
    for i in range(n):
        listt.append(next(gen))
    return listt
something=take(5,generator())
print(something)
#c squares_gen(limit) yielding squares of integers up to limit
def generating_squares(n):
    for i in range(n):
        yield i**2
somethingg=generating_squares(5)
print(list(somethingg))
#d Use both generators to print the first 10 Fibonacci numbers that are also perfect squares.
import math
def printing_everything(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b
some = printing_everything(10)
normal_nums = list(some)
print("fibo",normal_nums)
def perfect_squares(numbers):

    for i in numbers:
        root = math.sqrt(i)
        if root == int(root):
            yield i
somethings = perfect_squares(normal_nums)
print(list(somethings))
#d in one single thing 
def single_function(n):
    a=0
    b=1
    for i in range(n):
        somee=math.sqrt(a)
        if somee==int(somee):
            yield a
        a,b=b,a+b
functionn=single_function(10)
print("trying it in single function ")
print(list(functionn))  

#e
       
    
        
        
