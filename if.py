#def fact(n):
    #if n==0 or n==1:
   #     return 1
  #  else:
 #       return n*fact(n-1)
#n=int(input("enter a number: "))
#print(fact(n))#

#n=5
#fact=1
#for i in range(1,n+1):
   # fact*=i
  #  print(fact,end=" ")




#def facotr(n):
#    result=[]
 #   for i in range (1,n//2):
  #      if n%i==0:
   #         result.append(i)
   # result.append(n)
 #   return result
#n=int(input("enter a number: "))
#print(facotr(n))


                    

from math import sqrt 
def fac(n):
    result=[]
    for i in range(1,int(sqrt(n))+1):
        if n%i==0:
            result.append(i)
            if n//i!=i:
                result.append(n//i)
        result.sort()
        
    return result
n=int(input("enter A NUMBER:  "))
print(fac(n))

