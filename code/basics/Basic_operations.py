# user input
user_input=input("Enter number:")
if user_input.isdigit() :
  print(int(user_input)**2)
  pass
elif type(user_input)==str:
  print(f"Text is {user_input}")  
  pass
else:
  print("New datatype")