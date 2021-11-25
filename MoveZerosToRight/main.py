def move_zeros(array):
    lengthArray=len(array)
    MaximumNoIteration=lengthArray
    idx=0
    while idx<lengthArray and MaximumNoIteration!=0:
        if array[idx] == 0:
            array.pop(idx)
            array.append(0)
            MaximumNoIteration-=1
        else:
            idx+=1
    return array
