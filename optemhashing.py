a = [1,2,3,4,5,6,7,8,9]
b = [1,2,3,4,5,6,7,8,9,7,6,5,4,5,6,7,5,3,5,6,7,5,3,3,5,6,6]
hashi_mao = [0] * 11
for i in b:
    hashi_mao[i] += 1
for i in a:
    print(i, "appears", hashi_mao[i], "times")