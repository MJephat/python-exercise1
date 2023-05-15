# determine if a string is a palindrome.
#  checking if radar is a palindrome

# steps:
# find the reverse of the string or number
# check if the reverse and original are same or not.


print("Hello, world!")

def isPalindrome(h):
    h=h.lower()
    return h == h[:: -1]

h = "Python programs require"
jibu = isPalindrome(h)

if jibu:
    print("Yes! is a palindrome")
else:
    print("No! is not a palindrome")



# # iterative method.
# def isPalindrome(s):

# 	# Run loop from 0 to len/2
# 	for i in range(0, int(len(str)/2)):
# 		if str[i] != str[len(str)-i-1]:
# 			return False
# 	return True

# # main function
# s = "malayalam"
# ans = isPalindrome(s)

# if (ans):
# 	print("Yes")
# else:
# 	print("No")




# function to check string is
# palindrome or not
# def isPalindrome(j):
  
#     # Using predefined function to
#     # reverse to string print(s)
#     jina = ''.join(reversed(j))
  
#     # Checking if both string are
#     # equal or not
#     if (j == jina):
#         return True
#     return False
  
# # main function
# j = "malayalam"
# ans = isPalindrome(j)
  
# if (ans):
#     print("Yes")
# else:
#     print("No")
