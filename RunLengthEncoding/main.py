def runLengthEncoding(string):
    counter=0
    lastElement=""
    sol=""
    for i in string:
        if i == lastElement and counter<=7:
            counter+=1
            pass
        elif i !=lastElement or counter>7:
            counter+=1
            sol=sol+str(counter)+str(lastElement)
            counter=0
        lastElement=str(i)
    counter+=1
    sol=sol+str(counter)+str(lastElement)
    return sol[1:]
