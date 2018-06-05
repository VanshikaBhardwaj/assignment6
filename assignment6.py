#1
list1=list()
print("Enter 5 values to print")
i=0
while(i<5):
    i+=1
    list1.append(input())
print(list1)

#2
while(True):
    print("I will never end!")

#3
list2=list()
list3=list()
print("enter 10 values to list")
i=0
while(i<10):
    list2.append(int(input()))
    list3.append(list2[i]*list2[i])
    i+=1
print(list3)

#4
list4=["vanshika",45,23.756,2345,"32rf",3.6]
floatList=list()
intList=list()
strinList=list()
for i in range (len(list4)):
    a=type(list4[i])
    if(a==float):
        floatList.append(list4[i])
    elif(a==int):
        intList.append(list4[i])
    elif(a==str):
        strinList.append(list4[i])
print("float values=",floatList)
print("string values=",strinList)
print("int values=",intList)

#5
primeList=list()
for i in range (1,101):
    flag = 0
    for j in range(2,i//2):
        if(i%j==0):
            flag=1
            break
    if(flag==0):
        primeList.append(i)
print(primeList)

#6
for i in range(1,5):
    for j in range(1,i+1):
        print("*",end=" ")
    print("\n")

#7
listKey=list()
dict1={}
print("enter 4 value for a dictionary")
for i in range(0,4):
   listKey.append(input())
print("enter values")
for i in range(0,4):
    dict1[listKey[i]]=input()
print(dict1)


#8
print("enter 5 elements")
list5=list()
for i in range(0,5):
    list5.append(input())
elem=input("enter an element to be deeleted")
for i in range(0,5):
    if elem==list5[i]:
        list5.remove(elem)
        break
print(list5)