from unittest import result


num = input('Enter the numerator: ')
den = input('Enter the denominator: ')

try: 
  num = float(num)
except Exception as e:
  print('The numerator is not a number.')
  
try:
  den = float(den)
except Exception as e:
  print('The denominator is not a number.')

try:
  result = num/den
  print(f'The result of this division is {result}.')
except ZeroDivisionError as e:
  print('You cannot divide by 0.')
  print('This division cannot be performed.')
except Exception as e:
  print('This division cannot be performed.')
finally:
  print('Goodbye!')


