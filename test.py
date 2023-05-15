def reversed_string(word):
    str = " "
    for c in word:
        str = c + str
    return str
word = "loop"
    # print("the original string is: ", end="")
print(reversed_string(word))