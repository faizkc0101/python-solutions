#febinoci 
'''
def febinoci(n, a=0, b=1, sequence=None):
    if sequence is None:
        sequence = [a]
    if n == 1:
        sequence.append(b)
        print(sequence)
        return
    sequence.append(b)
    febinoci(n-1, b, a+b, sequence)

febinoci(10)
'''
   

#8)print the star pattern
'''
for i in range(6):
    for j in range(i):
        print(i,end='')
    print('')
'''
   
#7) Find the number of occurrences of a substring in a sting
'''
def count_substring(string,substring):
   count = string.count(substring)
   print(f'count of {substring} is {count}')
'''
'''
def count_substring(string):
    print(string)
    count = 0
    for i in range(len(string)-1):
        count += string[i:i+3] == 'the'
    print(count)


count_substring('the quick brown fox jumps over the lazy dog')
'''

#6) display numbers divisible by 5
'''
numbers = [10,34,30,423,23,45,20,34,10]

divisible= 5

true=[]
false=[]

for num in numbers:
    if num % divisible ==0:
        true.append(num)
    else:
        false.append(num)
print(true)
print(false)
'''

#5) check if the first and last number of a list is same
'''
def check_list(nums):
    if nums[0] == nums[-1]:
        return True
    else :
        return False

print(check_list([10,20,39,23,101]))
'''
# 4) Remove first n characters from a string
'''
def remove_chars(str,n):
    print(f'original {str}')
    return str[n:]

print(remove_chars('pyNative',4))
''' 

# 3) print characters present at even index number
'''
name = input('enter a string')

for i in range(0,len(name),2):
    print(name[i])
'''


# 2) print the sum of a current number and previous number
'''
class Print:

    def printSum(self,n):
        for i in range(n):
            current=i
            previous = i - 1
            if previous <0:
                previous=0
            sum = current+previous
            print (f'current number {current} previous number {previous} sum:{sum}')
obj = Print()
obj.printSum(10)
'''



# 1)calculate the multiplication and sum of two number
'''
def get_number(num1,num2):
    total = num1*num2
    if total <= 1000:
        return total
    else:
        return num1 + num2

print(get_number(100,12))    
'''





