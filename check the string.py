def reverse(text):
    return text[::-1]

def isPalindrome(text):
    rev = reverse(text)

    if (text == rev):
        return True
    return False

text = str(input("enter the text: "))

ans = isPalindrome(text)

if ans == 1:
    print("Yes")
else:
    print("No")



