# Mean
def mean(lst):
  mean = sum(lst)/len(lst)
  print(mean)


# Median
def median(lst):
  lst.sort()
  if len(lst) % 2 == 0:
      m1 = lst[len(lst)//2]
      m2 = lst[len(lst)//2 - 1]
      median = (m1 + m2)/2
  else:
      median = lst[len(lst)//2]
  print(median)


# Mode
def mode(lst):
  frequency = {}
  for i in list1:
      frequency.setdefault(i, 0)
      frequency[i]+=1

  frequent = max(frequency.values())
  for i, j in frequency.items():
      if j == frequent:
          mode = i
  print(mode)

#main
list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
mean(list1)
median(list1)
mode(list1)
