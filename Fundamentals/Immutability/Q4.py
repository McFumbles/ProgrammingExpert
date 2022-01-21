def replace(lst,target,swap_value):
  for x in range(len(lst)):
    element = lst[x]

    if element == target:
      lst[x] = swap_value