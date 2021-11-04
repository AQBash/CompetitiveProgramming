def threeNumberSum(array, targetSum):
    sol=[]
    array.sort()
    for idx, i in enumerate(array[:-2]):
        intermediateVar=targetSum-i
        l=1
        for jdx, j in enumerate(array[idx+l:-1]):
            for kdx, k in enumerate(array[jdx+idx+l+1:]):
                if intermediateVar-j ==k:
                    Ires=[i,j,k]
                    Ires.sort()
                    sol.append(Ires)
                else:
                    Ires=[]
    return sol
