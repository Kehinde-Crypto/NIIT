p = int(input('Enter the first value:'))
u = int(input('Enter the second value:'))
n = int(input('Enter the third value: '))

if p & u > 0:
  print('true')
elif u & n > 0:
  print('false')
elif p & n > 0:
  print('true')
else:
  print('false')
