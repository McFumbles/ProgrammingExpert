def find_all_odds(lst):
  odd = []
  for x in lst:
    if (x % 2) != 0:
      odd.append(x)
  return odd

print(find_all_odds([1,3,5,6]))
