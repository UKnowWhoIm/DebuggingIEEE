#input() -> int(input) to prevent TypeError
for i in range(int(input())): 
        word = input()
        # word.upper() returns the upper case version of string without changing the original string
        word = word.upper() 
        vowels = ['A','E','I','O','U']
        # '==' is uswed to compare, '=' is used to assign
        count = 0
        # range should be b/w 0 and len(word) - 1, as last char should be excluded not 1st char
        for j in range(len(word)-1):
                #vowels[] is not valid
                if word[j] in vowels:
                        # if j == 0 is an unwanted condition
                        if word[j+1] in vowels:
                                # count++ is not valid, count+= 1 is
                                # cout should be incremented
                                count += 1
                                break
                        else:
                                # count++ is not valid, count+= 1 is
                                count += 1
        print (count)
"""

SAMPLE INPUT-1
	 3
    	radeon
    	coir
    	malayalam
   

SAMPLE OUTPUT:1
  2
  1
  4

for i in range(input()): 
        word = input()
        word.upper() 
        vowels = ['A','E','I','O','U']
        count == 0 
        for j in range(1,length(word)) 
                if word[j] in vowels[]: 
                        if j = 0: 
                                count ++ 
                        elif word[j+1] in vowels[]: 
                                break
                        else:
                                count ++ 
        print (count) 

"""
