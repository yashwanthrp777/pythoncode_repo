#class bank:
    #def __init__(self,acc_no,balance):
      #  self.__acc_no=acc_no
     #   self.__balance=balance
    #def chick_balance(self,amount):
        #self.__balance+=amount
       # if self.__balance<amount:
      #      print("insuficent balance")
     #       return



    #def withdra(self,amount):
        #self.__balance-=amount  
        #print(f"{self.__balance} total amount in the account")

#a1=bank(acc_no=111,balance=500000)
#a1.withdra(500001)        



def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a//b

while(True):
  print("### simple calcluter####")
  print("1,addition")
  print("2 ,subrection")
  print("3, multipaction")
  print("4, subraction")
  print("5 , quict")

 
  choois=int(input("enter the number: "))
  if choois in {1,2,3,4}:
 
      a=int(input("enter the first number: "))
      b=int(input("enter the second number: "))

      if choois==1:
          print(f"{add(a,b)} addion of the number")
      elif choois==2:
          print(f"{sub(a,b)} subraction of the number")
      elif choois==3:
          print(f"{mult(a,b)} multiplication of the numbers")
      elif choois==4:
          print(f"{div(a,b)} division of the numbers")
  elif choois==5:
          print("quict the calcelater")
          break
  else:
       print("invalid numbers")        

