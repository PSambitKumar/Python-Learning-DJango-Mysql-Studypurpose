def palindromeNumber():
    number = int(input("Enter a Number?\n"))
    temp = number
    reversed = 0

    while temp != 0:
        reminder = temp % 10
        reversed = (reversed * 10) + reminder
        temp = temp // 10
    # print("Number is : " + str(number) + " and Reversed Number is : " + str(reversed))
    if number == reversed:
        print("Number is a Palindrome.")
    else:
        print("Number is Not a Palindrome.")


def palindromeString():
    string = input("Enter a String?\n")
    string = string.casefold()
    reversedString = string[::-1]
    if string == reversedString :
        print("String is a Palindrome.")
    else:
        print("String is not a Palindrome.")