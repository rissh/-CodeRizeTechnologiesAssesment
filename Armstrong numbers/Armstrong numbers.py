# your code goes here
def is_armstrong(nums):
 
    num_str = str(nums)
    n = len(num_str)
 
 
    armstrong_sum = 0
 
    for digit in num_str:
        armstrong_sum += int(digit) ** n
 
    return armstrong_sum == nums
 
 
num = 120                   # False
print(is_armstrong(num))
 
num = 370                   # True
print(is_armstrong(num))
