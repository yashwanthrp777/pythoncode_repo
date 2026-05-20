def pri(num):
    result=[]
    for i in range(1,num//2+1):
        if num%i==0:
            result.append(i)
    return result
num=int(input("enter a number: "))
print("the prime factors of the  number are:",pri(num))
