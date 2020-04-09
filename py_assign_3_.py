#Assignment-3
#first part
'''
def solution(A):
    s1=[]
    s2=[]
    n=len(A)
    p=0
    q=1
    l=[]
    while q<n and q!=n:
        sum1=0
        sum2=0

        s1=A[0:p+1]         #it will store the first part of array
        for i in s1:
            sum1+=i
            
        s2=A[p+1:n]         #it will store the second part of array
        for i in s2:
            sum2+=i
               
        d=abs(sum1-sum2)    #absolute difference between two parts
        l.append(d)
        p+=1
        q+=1
        
    l.sort()
    m=min(l)                #finding the minimal difference
    return m
        
          
A=[]
n=int(input("Enter the number of integers : "))
for i in range(n):
    A.append(int(input("Enter the integer : ")))
print("The given array is ",A)
print("The minimal difference is ", solution(A))

'''
#second part
#exception handling

def solution(A):
    s1=[]
    s2=[]
    n=len(A)
    p=0
    q=1
    l=[]
    while q<n and q!=n:
        sum1=0
        sum2=0

        s1=A[0:p+1]         #it will store the first part of array
        for i in s1:
            sum1+=i
            
        s2=A[p+1:n]         #it will store the second part of array
        for i in s2:
            sum2+=i
               
        d=abs(sum1-sum2)    #absolute difference between two parts
        l.append(d)
        p+=1
        q+=1
        
    l.sort()
    try:
         m=min(l)                #finding the minimal difference
         for i in l:
             if type(i)==int and len(l)>1:
                 return m
    except ValueError:
         print("Hey!! try to give more than one number")
         
    
   
          
A=[]
n=int(input("Enter the number of integers : "))
try:    
    for i in range(n):
        A.append(int(input("Enter the integer : ")))
except ValueError:
     print(" Please enter numbers only ")
print("The given array is ",A)
print("The minimal difference is ", solution(A))

