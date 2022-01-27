def create_strings_from_characters(frequencies, string1, string2):  
  able_string1 = able_to_create_string(frequencies,string1)
  able_string2 = able_to_create_string(frequencies, string2)

  if (not able_string1) or (not able_string2):
    if able_string1 or able_string2:
      return 1
  
    return 0

  for character in string1 + string2:
    if character not in frequencies or frequencies[character] == 0:
      return 1
    
    frequencies[character] -= 1
  
  return 2



def able_to_create_string(frequencies, string):
  for character in set(string):
    if string.count(character) > frequencies.get(character, 0):
      return False

  return True