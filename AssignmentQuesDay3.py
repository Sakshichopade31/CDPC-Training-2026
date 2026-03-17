"""
1.Write a program to check whether a number is even or odd.
2.Write a program to find the largest of three numbers.
3.Check whether a number is positive, negative, or zero.
4.Write a program to check whether a number is divisible by both 3 and 5.
5.Write a program to print numbers from 1 to N.
6.Write a program to print all even numbers from 1 to N.
7.Write a program to calculate the sum of first N natural numbers.
8.Write a program to calculate the factorial of a number.
9.Write a program to print the multiplication table of a number.
10.Write a program to count the number of digits in a number.
11.Write a program to reverse a number.
12.Write a program to check whether a number is palindrome.
13.Write a program to find the sum of digits of a number.
14.Write a program to check whether a number is an Armstrong number.
15.Write a program to print numbers divisible by 7 between 1 and N.
"""

#1.Write a program to check whether a number is even or odd.
"""
num = int(input("Enter number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
"""
#2.Write a program to find the largest of three numbers.
"""
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest =", a)
elif b >= c:
    print("Largest =", b)
else:
    print("Largest =", c)

"""
#3.Check whether a number is positive, negative, or zero.
"""
num = int(input("Enter number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

"""
#4.Write a program to check whether a number is divisible by both 3 and 5.
"""
num = int(input("Enter number: "))

if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both")

"""
#5.Write a program to print numbers from 1 to N.
"""
n = int(input("Enter N: "))

for i in range(1, n + 1):
    print(i)

"""
#6.Write a program to print all even numbers from 1 to N.
"""
n = int(input("Enter N: "))

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)

"""
#7.Write a program to calculate the sum of first N natural numbers.
"""
n = int(input("Enter N: "))

sum = 0
for i in range(1, n + 1):
    sum += i

print("Sum =", sum)

"""
#8.Write a program to calculate the factorial of a number.
"""
n = int(input("Enter number: "))

fact = 1
for i in range(1, n + 1):
    fact *= i

print("Factorial =", fact)
"""
#9.Write a program to print the multiplication table of a number.
"""
n = int(input("Enter number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)
"""
#10.Write a program to count the number of digits in a number.
"""
num = int(input("Enter number: "))

count = 0
while num != 0:
    num = num // 10
    count += 1

print("Digits =", count)
"""
#11.Write a program to reverse a number.
"""
num = int(input("Enter number: "))

rev = 0
while num != 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reversed number =", rev)
"""
#12.Write a program to check whether a number is palindrome.
"""
num = int(input("Enter number: "))
temp = num
rev = 0

while num != 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
"""
#13.Write a program to find the sum of digits of a number.
"""
num = int(input("Enter number: "))

sum = 0
while num != 0:
    digit = num % 10
    sum += digit
    num = num // 10

print("Sum of digits =", sum)
"""
#14.Write a program to check whether a number is an Armstrong number.
"""
num = int(input("Enter number: "))
temp = num
sum = 0

while num != 0:
    digit = num % 10
    sum += digit ** 3
    num = num // 10

if temp == sum:
    print("Armstrong number")
else:
    print("Not Armstrong")
"""
#15.Write a program to print numbers divisible by 7 between 1 and N.
"""
n = int(input("Enter N: "))

for i in range(1, n + 1):
    if i % 7 == 0:
        print(i)
"""