lessthan2 = 0
between2and5 = 0
between5and10 = 0
greaterorequalthan10 = 0
animal = str(input("Is there an animal to be recorded? (yes/no)")).lower()
while animal == "yes":
  age = int(input("Insert the age of the animal:"))
  if age < 2:
    lessthan2 += 1
  elif age in range(2,5):
    between2and5 += 1
  elif age in range(5,10):
    between5and10 += 1
  elif age >= 10:
    greaterorequalthan10 += 1
  an_animal = str(input("Is there another animal to be recorded? (yes/no)")).lower()
  if an_animal == "no":
    print(f"The number of animals with less than 2 years are {lessthan2}")
    print(f"The number of animals between 2 and 5 years are {between2and5}")
    print(f"The number of animals between 5 and 10 years are {between5and10}")
    print(f"The number of animals with 10 or more years are {greaterorequalthan10}")
    break
