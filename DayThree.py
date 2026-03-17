
"""
# Reversal of the number 
no = int(input("Enter the no. : "))
rev = 0 
while no > 0:
    rem = no % 10
    rev = rev*10 + rem 
    no = no // 10   #// remove karta hai last number ko as waha 10 hai 
print("Reverse is : ", rev )
-------------------------------------------------------------------------------
# Count the digits 
no = 123
count = 0 
while no>0 :
    one = no//10 
    count= count + 1 
print(count)
---------------------------------------------- 
# sum of  the  number 
no = int(input("Enter the no. : "))
sum = 0 
while no > 0 :
    rem = no %10 
    sum = sum + rem 
    no = no // 10  
print(sum)
---------------------------------------------- 
#palindrome 
no =  int(input("Enter the number :"))
rev = 0
temp = no 
while no > 0:
    rem = no % 10 
    rev = rev*10 + rem 
    no = no // 10 
if temp == rev :
     print("Palindrome")

else: 
    print("Not Palindrome ")
---------------------------------------------- 
#amstrong number 
no =  int(input("Enter the number :"))
sum = 0 
temp = no 
count= len(str(no))
while no >  0:
    rem = no  % 10 
    sum = sum + rem** count
    no = no // 10 
if temp == sum :
    print("armstrong")
else : 
    print("not armstrong")
    
digit= 123
count= len(str(digit)) 
print(count)
---------------------------------------------- 
# armstrong for range (again)
for i in range(1,10000):
   no =  i
   sum = 0 
   temp = no 
   count= len(str(no))
   while no >  0:
     no = no // 10 
     count = count + 1
 no = temp 
 while no >  0:
     rem = no  % 10 
     sum = sum + rem** count
     no = no // 10

 if temp == sum :
     print("armstrong", i  )
----------------------------------------------     
# Range ka sum 
n = int(input("Enter n: "))
x= int(input("Enter x :"))
sum = 1

for i in range(1,n):
    sum = sum + (x**i)/i
print(sum )   


"""