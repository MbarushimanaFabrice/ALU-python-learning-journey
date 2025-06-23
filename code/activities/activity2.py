# The program will keep prompting for the password until the correct one is entered.
# If the user enters the wrong password more than 2 times, an alert will be displayed.
# If the password is less than 8 characters, an error message will be displayed.
# If the password does not contain a digit, an error message will be displayed.

counter=0
# loop unitil user enters the correct password
while True:
  password= input("Enter password: ")
  if password== "secret123": 
    print("Access granted.")
    break
  counter=counter+1 # count the number of attempts
  if counter > 2:
      print("Alert: Too many attempts.")
  # Validate password length
  elif len(password) < 8:
    print("Error: Too short.")
    continue
  # Check for digits in the password
  digitNumber = 0
  for c in password:
    if c.isdigit():
      digitNumber =digitNumber+ 1
  if digitNumber == 0:
    print("Error: Need a digit.")
    continue
  else:
    print("Access denied.")
    continue
  