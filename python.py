'''
1) two sum
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
'''
def twoSum( nums, target):
        for i in range(len(nums)):

            for j in range(i + 1, len(nums)):
            
                if nums[i] + nums[j] == target:
                   
                    return [i, j]
# print(twoSum([1,2,3,4],5))

a = [1, 2, 3, 4, 5, 5, 3]
b = []
for i in a:
    if i not in b:
        b.append(i)
    else:    
        b.remove(i)
count = len(b) 

# print(a)
# print(count)    
# print(b)        

# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.

def isPalindrome(x):
    x_str =str(x)
    y=x_str[::-1]
    return x_str == y

# print(isPalindrome(342))
