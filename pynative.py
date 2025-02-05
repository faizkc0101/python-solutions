
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