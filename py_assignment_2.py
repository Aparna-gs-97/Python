
#Question-1

def solution(A,k):
    count=0
    while(count!=k):
        A=A[-1:]+A[0:-1]    #using slicing
        if count==k-1:
                print("The array after rotation  is ",A)
        count+=1


A=[]
num=int(input("Enter the number of elements of array: "))
for i in range(num):
    A.append(int(input("Enter the element: ")))
print("The given array is :",A)
k=int(input("Enter the number of times you want to rotate array: "))
solution(A,k)


#Question-2

def solution(X,Y,D):
    i=1
    current_pos=1
    count=0
    while(current_pos!=Y and current_pos<Y):
        current_pos=X+D*i
        i+=1
        count+=1
    print("The minimum number of jumps required by the frog : ",count)



X=int(input("\nEnter the initial position of the frog: "))
Y=int(input("\nEnter the position the frog wants to move : "))
D=int(input("\nEnter the fixed distance at which the frog moves: "))
solution(X,Y,D)









