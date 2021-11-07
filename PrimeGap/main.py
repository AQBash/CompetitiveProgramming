import math
def gap(g, m, n):
    def isPrime(p):
        j=round(math.sqrt(p))
        while j>1:
            quotient, remainder = divmod(p,j)
            if remainder ==0:
                return False
            j-=1
        return True
    idx=0
    firstPrime=None
    secondPrime=None
    for i in range(m, n+1):
        PrimeCandidate=m+idx
        found = isPrime(PrimeCandidate)
        idx+=1
        if found==True and firstPrime==None:
            firstPrime=PrimeCandidate
        elif found==True and firstPrime!=None:
            secondPrime=PrimeCandidate
        
        if firstPrime and secondPrime:
            gap=secondPrime-firstPrime
            if gap==g:
                return [firstPrime, secondPrime]
            else:
                firstPrime=secondPrime
                secondPrime=None
    return None