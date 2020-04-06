Input = []
n = int(input("Enter number of elements : "))
# To prevent ValueError
input_string = input().split(' ')
for i in range(0, n):
    # input() would be a string of numbers leading to ValueError
    ele = int(input_string[i]) 
    Input.append(ele)

if Input[0] < 0:
    # The sign of Input[0] is -ve, so prev = -1
    prev = -1
elif Input[0] > 0:
    # The sign of Input[0] is +ve, so prev = 1
    prev = 1
else:
    # Input[0] = 0 which has no sign
    prev = 0

#Initialize ans to 0
ans = 0

# To prevent checking Input[0] again, begin from Input[1]
for elem in Input[1:]:
    # '==' should be used instead of '='
    if elem == 0:
        # 0 has no sign
        sign = 0
    else:
        sign = elem / abs(elem)

    if sign == -prev:
        ans = ans + 1
    # this should be executed irrespective of previous condition
    prev = sign
# ans should be printed, not sign
print(ans)
"""

Input = [] 
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
    ele = int(input()) 
    Input.append(ele)
if(Input[0]<0):
    prev =1
else:
    prev=-1
for elem in Input: 
	if elem =0: 		
		sign = -1
	else: 
		sign = elem / abs(elem) 

	if sign == -prev: 		
		ans = ans + 1
		prev = sign  
print(sign)
"""
