def isPalindrome(num):
    num = int(num)
    temp = num
    rev = 0
    while num > 0:
        dig = num % 10
        rev = rev * 10 + dig
        num = num // 10
    if temp == rev:
        print("YES")
    else:
        print("NO")


a = int(input())
for _ in range(a):
    isPalindrome(input())
