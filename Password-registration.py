counter = 0
password = ""
while counter < 8:
  counter += 1
  letter = input("Enter a character of your password:")
  if letter.isalnum():
    password += letter
  else:
    print("Please input a letter or a number")

print(f"Your password is {password}")
