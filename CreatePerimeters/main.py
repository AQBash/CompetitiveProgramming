def perimeter(n):
    i=1
    j=1
    cnt=n-1
    resultarray=[1,1]
    while cnt!=0:
        k=i+j
        i=j
        j=k
        resultarray.append(k)
        cnt-=1
    return sum(resultarray)*4
