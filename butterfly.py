for n in range(0,26):
    pos=-1
    inc=1
    for i in range(0,n):
        if i >=(n/2): inc=-1
        pos += inc
        if i == n/2: pos +=1 
        for j in range(0,n):
            if pos >= j or pos>= n-1-j:print("*",end=" ")
            else:print(" ",end=" ")
        print()
    print()