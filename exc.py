"""def fun(nums):
    n=nums
    nod=len(str(nums))
    digit=0
    while n>0:
        last_digit=n%10
        digit+=last_digit**nod
        n=n//10
    if nums==digit:
        return True
    else:
        return False
nums=153
print(fun(nums))"""


""""def fun(nums):
    n=nums
    temp=0

    while n>0:
        last_num=n%10
        temp=temp*10+last_num
        n=n//10
    if temp==nums:
        return True
    else:
        return False
nums=122
print(f"{(fun(nums))}")"""""


"""def fun(nums):
    result=[]
    for i in range(1,nums//2):
        if nums%i==0:
            result.append(i)
    result.append(nums)
    return result
nums=20
print(f"{fun(nums)}") """

"""def fib(nums):
    if nums==0 or nums==1:
        return nums

    return fib(nums-1)+fib(nums-2)
nums=20
print(f"{fact(nums)}")"""

"""def fact(nums):

    if nums==0 or nums==1:
        return 1
    else:
         return nums* fact(nums-1)
print(f"{fact(12)}")"""



def menu():
    print("bamk statement")
    print("1,banka balance",/n "2,withdraw to bank,/n")





       

