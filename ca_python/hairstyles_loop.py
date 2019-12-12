hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
for price in prices:
  total_price += price
print("Total: $" + str(total_price))

average_price = total_price / len(prices)
print("Average Haircut Price: $" + str(average_price))

new_prices = [price - 5 for price in prices]
print("New Prices:")
print(new_prices)
print("New Prices Under 30:")
new_prices_under_30 = [price for price in new_prices if price<30]    
print(new_prices_under_30)

total_revenue = 0
for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]

print("Total Revenue: $" + str(total_revenue))
print("Average Daily Revenue: $" + str(total_revenue/7))

cuts_under_30 = []
for i in range(len(new_prices)-1):
  if new_prices[i]<30:
    cuts_under_30.append(hairstyles[i])
    
print(cuts_under_30)

drink_choices = ["coffee", "tea", "water", "juice", "soda"]
for drink in drink_choices:
  print(drink)

#Write your function here
def divisible_by_ten(nums):
  count = 0
  for num in nums:
    if num % 10 == 0:
      count += 1
  return count

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))

#Write your function here
def add_greetings(names):
  greeting = []
  for name in names:
    greeting.append("Hello, " + name)
  return greeting

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))

#Write your function here
def delete_starting_evens(lst):
#   if len(lst) > 0:
#     for i in lst:
#       if i % 2 == 0:
#         lst = lst[1:]
#       else:
#         break
#     return lst

#   while (len(lst) > 0 and lst[0] % 2 == 0):
#     lst = lst[1:]
#   return lst

  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst.pop(0)
  return lst

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

#Write your function here
def odd_indices(lst):
#   new_list = []
#   for i in range(1, len(lst), 2):
#     new_list.append(lst[i])
#   return new_list

  return lst[1::2]

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))

#Write your function here
def exponents(bases,powers):
  result = []
  for base in bases:
    for power in powers:
      result.append(base**power)
  return result

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))

#Write your function here
def larger_sum(lst1,lst2):
  if sum(lst1) >= sum(lst2):
    return lst1
  return lst2

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))

#Write your function here
def over_nine_thousand(lst):
  sums = 0
  for i in lst:
    if sums < 9000:
      sums += i
  return sums

#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))

#Write your function here
def max_num(nums):
  maximum = nums[0]
  for number in nums:
    if number > maximum:
      maximum = number
  return maximum

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))

#Write your function here
def same_values(lst1,lst2):
  index_num = []
  for i in range(len(lst1)):
    if lst1[i] == lst2[i]:
      index_num.append(i)
  return index_num

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

#Write your function here
def reversed_list(lst1,lst2):
#   lst2.reverse()
#   if lst1 == lst2:
#     return True
#   return False

  for i in range(len(lst1)):
    if lst1[i] != lst2[len(lst2) - 1 - i]:
      return False
  return True

#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))