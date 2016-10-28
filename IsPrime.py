##################################
# Author: Swapnali Gujar
#This program determines if entered number is a PRIME number or not
#If entered number is not a prime number, it gives the list of all the number, it is divisible by
####################################

number = input("Enter a number: ")
print ("You have entered: ", number)
number = int(number)
total_div = number-1
j=0
k=0
i=2
lst=[]
#append 1 at the start of the list
lst.append(1)
for i in range(2,total_div):
    j = j+1
    if number%i == 0:
       # print("Number: ", number,"is divisible by:", i)
        lst.append(i)
    else:
        k = k+1
#append the number at the end of the list
lst.append(number)
if(j==k):
    print("Number:", number, "is a PRIME number")
else:
    print("Number:", number, "is NOT a PRIME number")
    print("Number:", number, "is divisible by: ",lst[:])
    #for item in lst[:]:
     #   print(item, ", ")




