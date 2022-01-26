def pairs_sum_to_target(list1, list2, target):
  pairs = []

  for i, value in enumerate(list1):
    for j, value1 in enumerate(list2):
      if list1[i] + list2[j] == target:
        pairs.append([i,j])
  
  return pairs