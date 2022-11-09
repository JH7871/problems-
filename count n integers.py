

def countstrings(n, start):

	
	if n == 0:
		return 1
	cnt = 0
	
	# if last character in string is 'e'
	# add vowels starting from 'e'
	# i.e 'e','i','o','u'
	for i in range(start, 5):
	
		
		cnt += countstrings(n - 1, i)
	return cnt
	
def countVowelStrings(n):

	# char arr[5]={'a','e','i','o','u'};
	# starting from index 0 add the vowels to strings
	return countstrings(n, 0)

n = 1
print(countVowelStrings(n))

