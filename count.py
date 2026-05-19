n=int(input("enter a number:  "))
cou=0
while n>0:
    cou+=1
    n=n//10
    
print("Number of digits:", cou)