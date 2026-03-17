"""
# Addition using functions 
def add(x,y):
    res = x + y 
    print(res)

if __name__ =='__main__':
    a = int(input("Enter the number :"))
    b = int(input("Enter the number :"))
    add(a,b)
    
------------------------------------------------------
    
# function with parameter and return values
def add(x,y):
    res = x + y 
    return res 
   

if __name__ =='__main__':
    a = int(input("Enter the number :"))
    b = int(input("Enter the number :"))
    res = add(a,b)
    print(res)    
-------------------------------------------------
    
"""