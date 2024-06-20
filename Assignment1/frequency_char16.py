#Write a program in python that counts the frequency of each character in a string.
str1 = input("Enter a string")
all_freq ={}
for i in str1:
     if i in str1:
          all_freq[i]+= 1
     else:
          all_freq = 1
print(str(all_freq))               