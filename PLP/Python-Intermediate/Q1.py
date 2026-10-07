"""Topic: List/Dict Comprehensions, lambda, map, filter 
Given numbers = [3, 7, 12, 19, 24, 31, 40, 47, 56, 63]. Solve using ONLY comprehensions or functional tools: 
(a) List comprehension: all odd numbers squared. 
(b) filter() with a lambda: numbers divisible by 4. 
(c) map() with a lambda: each number zero-padded to 3 digits (e.g., 7 -> '007'). 
(d) Dict comprehension: {number: 'even'/'odd'} for all numbers. 
(e) Predict the output: nums = [1,2,3,4,5,6] odd_sq = [x**2 for x in nums if x%2 != 0] div2 = list(filter(lambda x: x%2==0, nums)) padded = list(map(lambda x: str(x).zfill(3), nums[:3])) print(odd_sq, div2, padded) 
"""
numbers=[3, 7, 12, 19, 24, 31, 40, 47, 56, 63]
odd_numbers=[]
for i in numbers:
    if i%2==1:
        odd_numbers.append(i)
print(odd_numbers)
odd_numbers=list(filter(lambda x:x%4==0,numbers))
print(odd_numbers)
padded=list(map(lambda x:str(x).zfill(3),numbers))
print(padded)
dictt={}
for num in numbers:
    if(num%2==0):
        dictt[num]="even"
    else:
        dictt[num]="odd"
print(dictt)            
        
