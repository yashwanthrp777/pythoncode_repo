def arm(n):
    num=n
    total=0
    nod=len(str(n))
    while num>0:
        digit=num%10
        total+=digit**nod
        num=num//10
    return total==n
n=int(input("enter a number: "))
print(arm(n))