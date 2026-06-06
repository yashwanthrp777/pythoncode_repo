def arm(num):
    temp=0
    nod=len(str(num))
    while num>0:
        dig=num%10
        temp+=dig**nod
        num=num//10
    if temp==num:
        print(f"{num} is an armstrong number")
    else:
        print(f"{num} is not an armstrong number")
num=int(input("enter the number:  "))
arm(num)

