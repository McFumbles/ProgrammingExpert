def compare_lists(lst1=[], lst2=[]):
  set1 = set(lst1)
  set2 = set(lst2)
  result = set1.intersection(set2)
  return len(result)
