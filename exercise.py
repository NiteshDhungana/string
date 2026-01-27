# reverse a string
print("This program is about reversing the string.\n")
a="Hello , My name is Nitesh"
reversed_a=a[::-1]
print(reversed_a)
vowel_count=0
consonent_count=0

 
#count vowels and consonent
print("\n\nThis program is for counting the vowels and s=consonent.\n")

for i in a.lower():
    if i.isalpha(): 
          if i in "aeiou":
              vowel_count+=1
            
          else:
              consonent_count+=1


print("consenet :",consonent_count)
print("vowels :",vowel_count)
        

#palindrome checker
print("\n\n\nThis program is for checking the palindrome...\n")
pal_wword="civic"
check_pal=pal_wword[::-1]
if pal_wword==check_pal:
     print("The given word is palindrome\n")
else:
     print("The given word is not palindrome\n")
        


