def game(n):
    totalNumberofFields = n*n
    totalNumberofFieldswithoutDiagonal = totalNumberofFields - n
    
    UpperhalfNumberofFields = totalNumberofFieldswithoutDiagonal/2
    if divmod(n,2)[1]==1:
        ValueofDiagonal=n*0.5    
        return [2*UpperhalfNumberofFields+n, 2]
    else:
        ValueofDiagonal=n*0.5
        return [UpperhalfNumberofFields+ValueofDiagonal]
