#Assignment-1


#Question1:

num=int(input("Enter any number upto which squares should print: "))
for i in range(0,num):
    sqr=i*i
    print('\n',sqr)

    

#Question2:

def runner_up(list):
    list.sort()
    m=max(list)
    count=0
    for i in range(0,len(list)):
        if list[i]==m:
            count+=1
            print("The runnerup's score is ",list[-(count+1)])
   

list=[]
n=int(input("Enter the number of scores  : ")) 
for i in range(n):
    list.append(int(input("Enter the score : ")))
print("\nThe entered scores are : ")
print(list)
runner_up(list)



#Question3:

string=str(input("Enter any string to swap cases : "))
print("\nThe swapped case of the given string is :",string.swapcase())



#Question4:


list=[]
l=int(input("Enter the number of elements in the list: "))
for i in range(l):
    list.append(int(input("Enter the element: ")))
print("\nThe provided list is : ",list)
print("\nThe odd indexed elements of the given list is :",list[1:l:2])

    


    







