def isValidSubsequence(array, sequence):
    LengthOfSequence=len(sequence)
	LengthOfArray=len(array)
	ids=LengthOfSequence-1
	ida=LengthOfArray-1
	cnt=0
	while ids>=0:
		while ida>=0:
			if sequence[ids]==array[ida]:
				ida-=1
				cnt+=1
				if cnt>=LengthOfSequence:
					return True
				break
			else:
				ida-=1
		ids-=1
	return False

