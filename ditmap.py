num=[1,2,3,1,2,3,4,4,5,5,6,7,56,45,4,
     4,4,7,7,]
dit_map={ }
for i in range(0,len(num)):
    if num[i] in dit_map:
        dit_map[num[i]]+=1
    else:
        dit_map[num[i]]=1
print(dit_map)
