# Write your max_num function here:
# def max_num(num1, num2, num3):
#   if num1 > num2 and num1 > num3:
#     return num1
#   elif num2 > num1 and num2 > num3:
#     return num2
#   elif num3 > num1 and num3 > num2:
#     return num3
#   else:
#     return "It's a tie!"

def max_num(num1, num2, num3):
  maximum = max(num1, num2, num3)
  if (maximum == num1 or maximum == num2) and maximum == num3:
    return "It's a tie!"
  elif maximum == num1 and maximum == num2:
    return "It's a tie!"
  else:
    return maximum
  
# Uncomment these function calls to test your max_num function:
print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(2, 3, 3))
# should print "It's a tie"

# Write your over_budget function here:
def over_budget(budget,food_bill,electricity_bill,internet_bill,rent):
  bills = food_bill + electricity_bill + internet_bill + rent
  return budget < bills

# Uncomment these function calls to test your over_budget function:
print(over_budget(100, 20, 30, 10, 40))
# should print False
print(over_budget(80, 20, 30, 10, 30))
# should print True

# Write your always_false function here:
# def always_false(num):
#   if 0 < num < 0:
#     return True
#   return False

def always_false(num):
  return num < num > num

# Uncomment these function calls to test your always_false function:
print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False