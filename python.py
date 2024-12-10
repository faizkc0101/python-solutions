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
'''
2) 
'''
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
'''
3)
Given an integer x, return true if x is a 
palindrome
, and false otherwise.
'''

def isPalindrome(x):
    x_str =str(x)
    y=x_str[::-1]
    return x_str == y

# print(isPalindrome(342))


'''
4)
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
'''
def removeElement( nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1  
        return k 

# print(removeElement([1, 2, 3, 4, 4, 5, 5], 4)) 
def searchInsert( nums, target):

    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

# print(searchInsert([1,7,3,4,6],2))

def list_to_integer(digits):
    number = 0
    for digit in digits:
        number = number * 10 + digit
       
    return number +1

# print(list_to_integer([1,2,3]))


def plusOne(self, digits):

 n = len(digits)


for i in range(n - 1, -1, -1):
    if digits[i] < 9:
        digits[i] += 1
        return digits  
    digits[i] = 0 

return [1] + digits