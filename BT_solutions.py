def palindromeCheck(my_string):
    if my_string == my_string[::-1]:
        print("Yes")
    else:
        print("No")


palindromeCheck(input())