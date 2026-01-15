str1=input("Enter a string: ")
str3=[]
str4=[]
str5=[]
for i in str1:
    if i.isalpha() and (i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        str3.append(i)
    elif i.isalpha() and (not i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        str4.append(i)
    elif i.isdigit():
        str5.append(i)

print("Number of vowels: ",len(str3),str3)
print("Number of consonants: ", len(str4), str4)
print("Number of numbers: ",len(str5),str5)