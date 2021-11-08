import math

def is_prime(num):
    if num<=1:
        return False
    q1,r1=divmod(num,1)
    if r1!=0:
        return False
    q2,r2=divmod(num,2)
    if r2==0 and num!=2:
        return False

    sqrtNum=round(math.sqrt(num))
    div=3
    while div<=sqrtNum:
        qdiv,rdiv=divmod(num,div)
        if rdiv==0:
            return False
        div+=2
    return True
