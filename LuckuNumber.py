'''
Created on Apr 8, 2016

@author: siddhi parkar
'''
from pip._vendor.requests.packages.urllib3.connectionpool import xrange
from pip._vendor.distlib.compat import raw_input

def sum_of_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s
        
def is_prime(num):
    if num > 1:
        for i in xrange(2,num):
            if num%i == 0:
                return False
        else:
            return True
    else:
        return False

def square_of_digits(n):
    s = 0
    while n:
        s += (n%10)**2
        n //= 10
    return s

def is_lucky_num(num):
    num1 = sum_of_digits(num)
    num2 = square_of_digits(num)
    if is_prime(num1) and is_prime(num2):
        return num
    return False
def get_tc():
    test_cases = int(input())
    if( test_cases <1 and test_cases> 1000):
        get_tc()
    return test_cases           
if __name__=="__main__":
    test_cases = get_tc()
    arr =[]
    if test_cases == 1:
        numbers = raw_input()
        array = numbers.split()
        
        if len(arr) == 1:
            num1 = 1
            num2 = int(num1)
        else:
            num1 = int(array[0])
            num2 = int(array[1])
            arr.append([num1, num2]) 
        
    else:
        for tc in xrange(0,test_cases):
            numbers = raw_input()
            array = numbers.split()
            
            if len(array) == 1:
                num1 = 1
                num2 = int(num1)
            else:
                num1 = int(array[0])
                num2 = int(array[1]) 
            arr.append([num1, num2])   
            
    for ar in arr:
        num1 = ar[0]
        num2 = ar[1]
        count = 0
        for num in xrange(num1, num2):
                result = is_lucky_num(num)
                if result is not False:
                    count += 1
        print(count)