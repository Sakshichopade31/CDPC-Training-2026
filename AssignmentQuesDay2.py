"""
1.Write a program to calculate the perimeter of a rectangle using length and width entered by the user.
2.Write a program to convert kilometers into meters and centimeters.
3.Write a program to calculate the total bill amount if a user buys 3 products (take price of each product as input).
4.Write a program to convert hours into minutes and seconds.
5.Write a program to calculate the total number of seconds in a given number of days.

"""

#1.Write a program to calculate the perimeter of a rectangle using length and width entered by the user.
"""
l = int(input("Enter the length:"))
w = int(input("Enter the width:"))
peri = 2*(l * w)
print("Perimeter:",peri)
"""

#2.Write a program to convert kilometers into meters and centimeters.
"""
km = float(input("Enter distance in kilometers: "))
meters = km * 1000
centimeters = km * 100000

print("In meters =", meters)
print("In centimeters =", centimeters)
"""

#3.Write a program to calculate the total bill amount if a user buys 3 products (take price of each product).
"""
p1 = int(input("Enter price of PRODUCT 1 :"))
p2 = int(input("Enter price of PRODUCT 2 :"))
p3 = int(input("Enter price of PRODUCT 3 :"))
bill = p1 + p2 + p3

print("TOTAL BILL OF THE PURCHASED PRODUCTS IS :",bill)
"""
#4.Write a program to convert hours into minutes and seconds.
"""
hours = float(input("Enter time in hours: "))
minutes = hours * 60
seconds = hours * 3600

print("In minutes =", minutes)
print("In seconds =", seconds)
"""

#5.Write a program to calculate the total number of seconds in a given number of days.
"""
days = int(input("Enter number of days: "))
seconds = days * 24 * 60 * 60

print("Total seconds =", seconds)
"""