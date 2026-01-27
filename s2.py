txt ="I am learning python cuz in the future I want work as AI engineer in Big companies."
s_word=input("Enter any word you want to search in txt:")
if s_word in txt:
    print("yes,",s_word,"is present in txt.")
else:
    print("No,",s_word ,"is not present in txt")
