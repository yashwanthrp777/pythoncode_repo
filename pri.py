from math import sqrt
def pri(num):
    result=[]
    for i in range(1,int(sqrt(num))+1):
        if num%i==0:
            result.append(i)
    if num//2==0:
     result.append(num//i)
num=int(input("enter the number: "))
print("the prime factors of the number are: ",pri(num))
