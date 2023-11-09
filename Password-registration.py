counter = 0
password = ""
while counter < 8: 
  letter = input("Enter a character of your password:")
  if len(letter) == 1 and letter.isalnum():
    counter += 1
    password += letter
  elif len(letter) > 1:
    print("Please input one character at a time")
  else:
    print("Please input a letter or a number")

print(f"Your password is {password}")
