'''This findes that the given inputs 2 arrays/string have same elements in it'''

def count_ele(arr):
  d = {}
  for i in arr:
    if i in d:
      d[i] += 1
    else:
      d[i] = 1
  return d
arr1 = 'states'
arr2 = 'stsate'
s1 = count_ele(arr1)
s2 = count_ele(arr2)
if s1 == s2:
  print( 'both have same elements ')
else:
  print('both have diffrent elements : ')
