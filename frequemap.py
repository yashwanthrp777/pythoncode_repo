num=[3,5,3,8,5,3,8,9,5,4,3,6,7,8,6,2,1,23,5]
freq_map={}
for n in num:
    freq_map[n]=freq_map.get(n,0)+1

print(freq_map)
print('frequency of 2:', freq_map.get(2,0))
        