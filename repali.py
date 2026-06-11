def pali(s,left,right):
   
    if left<=right:
       return True
    if s[left]!=s[right]:
       return False
    return pali(s,left+1,right-1,)
s=(input("enter the  number: "))

print(pali(s,0,len(s)-1))