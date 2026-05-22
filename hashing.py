a=[1,2,3,4,5,6,7,8,9]
b=[1,2,3,4,5,6,7,8,9,7,6,5,4,5,6,7,5,3,5,6,7,5,3,3,5,6,6,]
for i in a:
    count=0
    for j in b:
        if j==i:
            count+=1
    print(i,'is present in b',count,'times')    
