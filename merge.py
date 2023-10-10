def merge_lists(list1, list2):
  """Merges two unsorted lists into a sorted result"""
  
  merged = []

  i = j = 0

  while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
      merged.append(list1[i])
      i += 1
    else:
      merged.append(list2[j])
      j += 1

  merged.extend(list1[i:])
  merged.extend(list2[j:])

  return merged

if __name__ == "__main__":

  # Test case 
  list1 = [1, 5, 3, 9]
  list2 = [6, 2, 4]

  merged = merge_lists(list1, list2)

  # Sort after merging
  merged.sort()

  print(merged) # [1, 2, 3, 5, 7, 8]
