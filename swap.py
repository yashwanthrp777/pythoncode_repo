def fact(n):
    if n<=1:
        return n
    return fact(n-1)+fact(n-2)
n=int(input("enter a number:  "))
for i in range(n):
    print(fact(i),end=" ")
