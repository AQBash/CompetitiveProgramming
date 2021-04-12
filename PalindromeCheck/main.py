def isPalindrome(string):
    # check if string is odd or even
	StringList=list(string)
	length=len(StringList)

	idx=0

	while idx<length:
		if StringList[idx]!=StringList[-idx-1]:
			return False
		else:
			idx+=1
	return True

	
    pass
