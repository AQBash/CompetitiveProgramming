def dbl_linear(n):
    liste=[1]
    operations=0
    for i in liste:
        operations+=1
        y=2*i+1
        liste.append(y)
            
        z=3*i+1
        liste.append(z)
        if operations>=5*n:#I don't like this solution
            liste = list(dict.fromkeys(liste))
            liste.sort()
            return liste[n]  
