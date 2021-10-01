#palindrome
str = input("Enter string: ")
is_palindrome = True

for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            is_palindrome = False

if is_palindrome:
    print(str, "is a palindrome")
else:
    print(str, "is not a palindrome")
