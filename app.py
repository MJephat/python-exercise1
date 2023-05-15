# determine if a string is a palindrome.
#  checking if radar is a palindrome

# steps:
# find the reverse of the string or number
# check if the reverse and original are same or not.


print("Hello, world!")

def isPalindrome(h):
    return h == h[:: -1]

h = "radar"
jibu = isPalindrome(h)

if jibu:
    print("Yes! is a palindrome")
else:
    print("No! is not a palindrome")





