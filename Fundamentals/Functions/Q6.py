def running_sums(numbers):
  lst = []

  current_number = 0
  for number in numbers:
    current_number += number
    lst.append(current_number)
  return lst
