#Palindrome Questions 
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        rev = 0
        
        while x > rev:
            digit = x % 10
            rev = rev * 10 + digit
            x = x // 10
        
        return x == rev or x == rev // 10
"""

# 1672. Richest Customer Wealth
""" 
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = []
        sum = 0
        for i in accounts:
            sum = 0
            for j in range(len(i)):

                sum = sum + i[j]
            wealth.append(sum)
        return max(wealth)
        
"""
#HACKEREARTH QUESTION : You have been given an array A of size N consisting of positive integers. 
# You need to find and print the product of all the number in this array Modulo 

"""
n = int(input())
arr = list(map(int, input().split())) 
mod = (10**9)+7
product = 1
for num in arr:
    product = (product * num) % mod

print(product)
"""
# #HACKERRANK QUESTION : Staircase Question 
"""

"""

#HACKERRANK QUESTION
#Given five positive integers, find the minimum and maximum values that can be calculated by 
# summing exactly four of the five integers. 
# Then print the respective minimum and maximum values as a single line of two
# space-separated long integers.
"""
import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    total = sum(arr)
    
    min_val = min(arr)
    max_val = max(arr)
    
    min_sum = total - max_val
    max_sum = total - min_val
    
    print(min_sum, max_sum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
    
    
"""

#You are in charge of the cake for a child's birthday. 
# It will have one candle for each year of their total age. 
# They will only be able to blow out the tallest of the candles. 
# Your task is to count how many candles are the tallest.

"""
import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    max_height = max(candles)
    count = candles.count(max_height)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
"""
#Given a time in -hour AM/PM format, 
#convert it to military (24-hour) time.
"""

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    period = s[-2:]        
    time = s[:-2]          
    
    hour = int(time[:2])
    
    if period == "AM":
        if hour == 12:
            hour = 0
    else:  # PM
        if hour != 12:
            hour += 12
    
    return f"{hour:02d}{time[2:]}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
"""
print("hello")


