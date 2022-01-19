string = input('Enter a string: ')

character_frequencies = {}

for character in string:
  character_frequencies[character] = character_frequencies.get(character, 0) + 1

for key in character_frequencies:
  freq = character_frequencies[key]
  print(f'{key}: {freq}')
