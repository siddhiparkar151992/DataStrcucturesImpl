'''
Created on Apr 23, 2016

@author: Dell
'''

workbook = []
def get_special_chapter(ar,max_num_al):
    count = 0
    
    for i,chapters in enumerate(ar):
        chapters =  int(chapters)
        if chapters >=1 and chapters <=100:
            arr = []
            for problem in range(chapters):#1 to 4
                if len(arr) is not 0 and len(arr[len(arr)-1]) < max_num_al:
                    arr[len(arr)-1].append(problem+1)
                else:
                    arr.append([problem+1])
            
            workbook.append(arr)
        else:
            return
    for i,chap in enumerate(workbook):
        for p in chap:
            if i+1 in p:
                count+=1
                break
                
    return count
if __name__ == '__main__':
    #arr= [4,2,6,1,10]
    #max_num = 3
    first = str(input())
    first = first.split()
    length= int(first[0])
    max_num= int(first[1])
    
    if length >=1 and length <=100 and max_num >=1 and max_num <=100:
        arr =  input().split(" ")
    print(get_special_chapter(arr, max_num))
    