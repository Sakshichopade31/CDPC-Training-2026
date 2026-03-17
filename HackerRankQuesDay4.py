#Questions 
"""
Q.1
if __name__ == '__main__':
    print("Hello, World!")
--------------------------------------
Q.2
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")
---------------------------------------
Q.3
if __name__ == '__main__':
    a = int(input())
    b = int(input())
sum = a + b 
print(sum)
diff = a - b
print(diff)
pro = a*b 
print(pro)
----------------------------------------
Q.4
if __name__ == '__main__':
    a = int(input())
    b = int(input())
div = a // b
print(div)
fl = a / b
print(fl)
----------------------------------------
Q.5
if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        c= i**2
        print(c)
----------------------------------------
Q.6
def is_leap(year):
    leap = False
    if ((year%4==0 and year%100!=0)or (year%400==0)):
        leap = True 
    
    return leap

year = int(input())
print(is_leap(year))    



"""