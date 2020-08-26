# given number is even or not
# a=int(input("Enter the number:\t"))
# if a%2 ==0 :
#     print("Given number {} is even number.".format(a))
# else:
#     print("Given number {} is odd number.".format(a))

# l=int(input("Enter the lower limit:\t"))
u=int(input("Enter the upper limit:\t"))
print("Even numbers:")
for num in range(1,u+1):
    if num%2 ==0:
        print(num)
print("Odd numbers:")
for n in range(1,u+1):
    if n==1 or n%2==1:
        print(n)



