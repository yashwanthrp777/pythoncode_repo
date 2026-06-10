s="nitin"
n=len(s)
left=0
right=n-1
while left<=right:
    if s[left]!=s[right]:
        print("false")
    left+=1
    right-=1
else:
    print("true")
    



