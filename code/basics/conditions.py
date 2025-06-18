try:
  number=int(input("Enter number: "))
  if number%2==0:
    print("Even number")
  elif number%2!=0:
    print("Odd number")
  else:
    print("opps !")
except ValueError:
  print("Opps!")