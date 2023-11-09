fresponse='yes'



while fresponse!='yes' and fresponse!='no':
  print('that is not a valid optio, try again')
  response=input()
  fresponse=str(response.lower())
while fresponse=='yes':
  print('We are going to calculate your total salary')
  print('But first, give me your name')
  name=input()
  print('Put here your base salary')
  basesalary=float(input())
  print('And how much you have made from sales')
  salesmade=float(input())
  if salesmade<3500:
    prefinalsalary=salesmade*0.07
    finalsalary=basesalary+prefinalsalary
    print('You total salary is ',finalsalary,name)

  elif salesmade>=3500 and salesmade<7000:
    prefinalsalary=salesmade*0.10
    finalsalary=basesalary+prefinalsalary
    print('You total salary is ',finalsalary,name)

  elif salesmade>7000:
    prefinalsalary=salesmade*0.15
    finalsalary=basesalary+prefinalsalary
    print('You total salary is ',finalsalary,name)

  else:
    fresponse='no'
    

  print('if there is another seller (yes/no response)')
  response=str(input())
  fresponse=str(response.lower())
