fin_arr= []  
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

arr = []
def U(x,y,arr):
    try:
        arr = fin_arr
        arr[x+1] = y
        return arr
    except Exception as e:
        
        arr = arr + [None]*x
        
        arr[x] = y
        return arr
def C(x,y,arr):
    sum =0
    if x==y:
        return F(x)
    else:
        for i in range(x-1,y):
            sum+= F(fin_arr[i])
    return sum
            
        
        
def F(x):
    a = range(x)
    if x ==1:
        return 1
    result = 0
    for i in range(1,x+1):
        result+= gcd(i,x)
            
            
    return result
  
if __name__ == "__main__":
    import itertools
    combs = []
    arr = [3,4,3]
    #print(C(1,3,arr))
    length_of_arr = int(input())
    if length_of_arr>=1 and  length_of_arr <= (10**6):
        arr = input().split(" ")
        
        for i in arr:
            temp = int(i)
            if temp >=1 and temp <=5*(10**5):
                global fin_arr
                fin_arr.append(temp)
        queries = int(input())
        output = []
        if(queries>=1 and queries <= (10**5)):
            for q in range(queries):
                lin =  input().split(" ")
                type = lin[0]
                q1 =int(lin[1])
                q2= int(lin[2])
                if q1>=1 and q1 <= length_of_arr:
                    if type  =="C":
                        r =C(q1,q2,fin_arr)
                        output.append(r)
                        
                    elif type=="U":
                        fin_arr = U(q1,q2,fin_arr)
            for k in output:
                print(k)     
                        
                    
                
                
        
                
                