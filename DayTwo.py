"""
## accept the 3 digit number and find the sum of that number 

 NOTE : kisi bhi number ko divide by 10 kiya toh uska last number milta hai 

n= 123
a = 1
b= 2
c = 3
sum = a + b + c
print(n)
print(sum)

-------------------------------------------------------------
# find last digit number 
no = int(input("Enter number :"))
res = no % 10  
print(res)
-------------------------------------------------------------
#sum oof two digits 

no = 45 
separate numbeer 4 and 5 
sum 4+5 = 9
kisi bhi number ko divide by 10 kiya toh uska last number milta hai 


no = int(input("Enter number :"))
n1 = no % 10  #5
n2 = no // 10 #4
res = n1 + n2 
print(res)
-------------------------------------------------------------

#sum of three number 
no = int(input("Enter number :"))
n1 = no % 10
no = no//10 
n2 = no % 10 
no = no // 10
n3 = no % 10 
res = n1 + n2 + n3 
print(res)

-------------------------------------------------------------
#sum of six numbers 
no = int(input("Enter the number "))
n1 = no % 10 
no = no // 10 
n2 = no % 10 
no = no // 10 
n3 = no % 10 
no = no // 10 
n4 = no % 10 
no = no // 10 
n5 = no % 10 
no = no // 10 
n6 = no % 10 
res = n1 + n2 + n3 + n4 + n5 + n6 
print(res)
-------------------------------------------------------------
# TASK : Reverse of 6 digits 
no = int(input("Enter the number "))
n1 = no % 10 
no = no // 10 
n2 = no % 10 
no = no // 10 
n3 = no % 10 
no = no // 10 
n4 = no % 10 
no = no // 10 
n5 = no % 10 
no = no // 10 
n6 = no % 10 
res = n1*100000 + n2*10000 + n3*1000 + n4*100 + n5*10 - n6 
print(res)
-------------------------------------------------------------
# accept the 9 digit no and find the sum of 
#1st and the last digit in 3 steps 
no = 123456789
n1 = no % 10
n2 = no // 100000000
res = n1 + n2 
print(res)
--------------------------------------------------------------
# TA = 20%, DA = 30% , HRA = 40%
no = int(input("Enter Basic Salary : "))
ta= no * 20 / 100
da = no * 30 / 100 
hra  =  no * 40 /100 
gs= no + ta + da + hra 
print(gs)
"""
n= 123
a = 1
b= 2
c = 3
sum = a + b + c
print(n)
print(sum)
