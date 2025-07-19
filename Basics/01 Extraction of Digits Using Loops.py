# Extraction of Digits Using Loops

n = 5873 
num = n 
while num > 0:
    last_digit_reminder = num%10
    print(last_digit_reminder, end=' ')
    num = num // 10
    