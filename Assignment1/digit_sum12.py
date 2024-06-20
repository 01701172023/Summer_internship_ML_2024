#12. Write a python program that calculates the sum of the digits of a given number.
number = int(input())
count =0
while number!= 0:
    number //= 10
    count += 1

print("Number of digits: " + str(count))