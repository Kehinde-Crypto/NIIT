# NESTED if statement
age = int(input('Please enter your age:'))
country = str(input ('please enter your country:'))
#age = 22

if age >= 18:
  print('You are an adult')
  if country == 'Nigeria':
    print('Can vote in nigeria')
  else:
    print('You are not a citizen') 
     
else:

  print('You are not an adult yet. ')