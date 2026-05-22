def pat(n):
    for i in range(n):
        for j in range(i+1):
            if i%2==0:
                print("0",end=" ")
            else:
                print("1",end=" ")
        print()
pat(5)                    