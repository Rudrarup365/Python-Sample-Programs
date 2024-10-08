
number = 1221
temp = number
reverse = 0
while number > 0:
    reminder = number % 10
    reverse = reverse * 10 + reminder
    number = int(number / 10)
if temp == reverse:
    print('Palindrome')
else:
    print('not palindrome')


