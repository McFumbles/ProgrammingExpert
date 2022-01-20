number = set()

while True:
  string = input('Enter a character: ')  
  if len(string) > 1:
    break

  if string in number:
    break

  number.add(string)

print(f'Number of unique characters entered: {len(number)}')
