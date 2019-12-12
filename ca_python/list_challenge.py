#Write your function here
def double_index(lst,index):
  if index < len(lst):
    lst[index] = lst[index] * 2
    return lst

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))

#Write your function here
def remove_middle(lst,start,end):
  if end < (len(lst) - 1):
    lst = lst[:start] + lst[end+1:]
    return lst

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

#Write your function here
def more_than_n(lst, item, n):
  if lst.count(item) > n:
    return True

#Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

#Write your function here
def more_frequent_item(lst,item1,item2):
  if lst.count(item1) > lst.count(item2):
    return item1
  elif lst.count(item1) < lst.count(item2):
    return item2
  else:
    return "Equal"
  
#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

#Write your function here
def middle_element(lst):
  if len(lst) % 2 != 0:
    lst[int(len(lst) / 2)]
    return lst
  else:
    lst_even = (lst[int((len(lst) / 2) - 1)] + lst[int(len(lst) / 2)]) / 2
    return lst_even

#Uncomment the line below when your function is done
print(middle_element([5, 2, -4, 4, 5]))
print(middle_element([5, 2, -10, -4, 4, 5]))

#Write your function here
def append_sum(lst):
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  return lst

def append_sum2(lst):
  for n in range (0,3):
    sum = lst[-2] + lst[-1]
    lst.append(sum)
  return lst

#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))
print(append_sum2([1, 1, 2]))

#Write your function here
def larger_list(lst1,lst2):
  if len(lst1) > len(lst2) or len(lst1) == len(lst2):
    return lst1[-1]
  elif len(lst1) < len(lst2):
    return lst2[-1]
  
#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

#Write your function here
def combine_sort(lst1,lst2):
  new_lst = lst1 + lst2
  new_lst.sort()
  return new_lst

#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

#Write your function here
def combine_sort(lst1,lst2):
  return sorted(lst1 + lst2)

#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

#Write your function here
def every_three_nums(start):
  if start <= 100:
    return list(range(start,101,3))
  return []

#Uncomment the line below when your function is done
print(every_three_nums(91))