textInputStr = input(str("Enter a string value to reverse from the command line: "))
lengthOriginalMessageInt = len(textInputStr)
newMessageStr = ""  
brandnewMessageStr = ""
for reversedmyCountInt in range(lengthOriginalMessageInt-1, -1, -1):
 newMessageStr = newMessageStr + textInputStr[reversedmyCountInt]
print(newMessageStr)
for myCountInt in range(0, lengthOriginalMessageInt, 1):
    brandnewMessageStr = brandnewMessageStr + textInputStr[myCountInt]
if(newMessageStr.lower() == brandnewMessageStr.lower()):
   print("This is a palindrome!!!(It is the same word spelled backwords)")
else:
   print("This is not a palindrome!!!")
