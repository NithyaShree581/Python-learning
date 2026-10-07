"""
Topic: Exception Patterns & Clean Code 
Refactor: def f(x,y): try: return x/y except: pass 
(a) Rename parameters, add a proper docstring (Args + Returns + Raises). 
(b) Handle ZeroDivisionError and TypeError separately with specific messages. 
(c) Add type hints: (dividend: float, divisor: float) -> Optional[float]. 
(d) Write batch_divide(pairs: list[tuple]) calling safe_divide, skipping failures, logging warnings. 
(e) Predict the output: from typing import Optional def safe_divide(a: float, b: float) -> Optional[float]:     try:         return a / b     except ZeroDivisionError:         print('Zero error')         return None results = [safe_divide(10,2), safe_divide(6,0), safe_divide(9,3)] print(results) 
"""
from typing import Optional
import logging
logging.basicConfig(level=logging.DEBUG)
def division_Stuff(x:int , y:int)->Optional[int]:
    try: 
        res=x/y
        return res
    except ZeroDivisionError: 
         logging.error("zero division error has been occured")
         return None  
    else:
        print("the operation is successful")
something=division_Stuff(2,6)
print(something)
something=division_Stuff(1,0)
print(something)

import logging

# for muliple pairs how can do this stuff
logging.basicConfig(level=logging.ERROR)
def multiple_division(x:list[float],y:list[float])->None:
    if(len(x)!=len(y)):
        print("there is some value misssing in either of the pair ")
        return
    for i in range(len(x)):
        try: 
            res=x[i]/y[i]
            print(res)
        except ZeroDivisionError:
            logging.error("an error has been occured")
        else:
            print("the operation is successful")
    return 
multiple_division([1,2,3,4,4],[2,3,4,5,0])
    
    
