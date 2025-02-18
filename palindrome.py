def reverse(string) -> str:
    out = ""
    for i in range(len(string), 0, -1):
        out += string[i-1]
    return out

word = input("enter a word: ")
if word == reverse(word):
    print("wow that is a palindrome!")

