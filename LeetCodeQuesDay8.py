#TWO SUM QUESTION
"""
class Solution:
    def twoSum(self, nums, target):
        num_map = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in num_map:
                return [num_map[complement], i]

            num_map[nums[i]] = i
"""  
# Fizz Buzz Question 
"""
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i  in range(1,n+1):
            if (i % 3 == 0 and i % 5 == 0):
                result.append("FizzBuzz")
            elif i % 3 == 0:
             result.append("Fizz")
            elif  i % 5 == 0:
             result.append("Buzz")
            else :
                result.append(str(i))

        return result

"""    
#Product of Array Except Self:
#○ Question: Given an array, return an array where each element is the product of all the elements in the array except itself.
#○ Logic: Use two passes, one from left to right, and one from right to left, to calculate products.
#○ Sample Input: [1, 2, 3, 4]
#○ Expected Output: [24, 12, 8, 6]

def productExceptSelf(nums):
    
    n = len(nums)
    result = [1] * n

    # Left pass
    left = 1
    for i in range(n):
        result[i] = left
        left *= nums[i]

    # Right pass
    right = 1
    for i in range(n-1, -1, -1):
        result[i] *= right
        right *= nums[i]

    return result
