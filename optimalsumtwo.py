def funct(nums):
    hashi_map={ }
    for i in range(0,len(nums)):
       result=target-nums[i]
       if result in hashi_map:
           return [hashi_map[result],i]
    hashi_map[nums[i]]=i 
nums=[9,2,1,4,5,6,8]
target=13       
print(f"{funct(nums)}")
