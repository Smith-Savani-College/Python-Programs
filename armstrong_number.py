num = int(input("Enter the number:"))
digits = 0
temp = num
while(temp):
    temp = temp//10
    digits = digits + 1

# print (digits)
temp = num
sum = 0
while(temp):
    digit = temp%10
    sum = sum + pow(digit,digits)
    temp = temp//10

if(sum == num):
    print ("The number is armstrong number")
else:
    print ("The number is not a armstrong number")
