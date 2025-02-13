# star pattern
'''
for i in range(6,0,-1):
    for j in range(i):
        print("*",end='')
    print('')
'''
#13 ) multiple table
'''
for i in range(1,11):
    for j in range(1,11):
        print(i,'*',j,'=',i*j)
    print('ff')
'''    
#12) calculate income tax

'''
income = int(input('enter your income'))
tax_payable = 0
print("Given income", income)

if income <= 10000:
    tax_payable = 0
elif income <= 20000:
    # no tax on first 10,000
    x = income - 10000
    # 10% tax
    tax_payable = x * 10 / 100
else:
    # first 10,000
    tax_payable = 0

    # next 10,000 10% tax
    tax_payable = 10000 * 10 / 100

    # remaining 20%tax
    tax_payable += (income - 20000) * 20 / 100

print("Total tax to pay is", tax_payable)
'''

# 11)Get each digit from a number in the reverse order.
'''
number = 1234
print(number)
while 0 < number :
    mod = number % 10
    number = number //10
    print(mod,end='')

'''


#10)merge two list the following condition
'''
def merge():

    l1 = list(map(int, input('Enter first list:  ').split(',')))
    l2 = list(map(int, input('Enter second list :').split(',')))
    list3=[]

    sample = l1+ l2
    for i in sample:
        if i % 5==0:
            list3.append(i)
    print(list3)
        
merge()
'''


#9)check palindrome numbers
'''
def revere(num):
    num2 = 0 
    while num > 0:
        rem = num % 10
        num2 = (num2*10)+rem
        num = num // 10
    return num2


print(revere(123))
'''
'''
def check(num):
    num1=str(num)
    num2 =num1[::-1]
    if num1 == num2:
       print('yes')
    else:
        print('no')

check(121)
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





