def ground(weight):
#   if weight >= 10:
#     ground_cost = 4.75 * weight + 20
#     return ground_cost
#   elif weight >= 6:
#     ground_cost = 4.00 * weight + 20
#     return ground_cost
#   elif weight >= 2:
#     ground_cost = 3.00 * weight + 20
#     return ground_cost
#   else:
#     ground_cost = 1.50 * weight + 20
#     return ground_cost
  if weight >= 10:
    price_per_weight = 4.75
  elif weight >= 6:
    price_per_weight = 4.00
  elif weight >= 2:
    price_per_weight = 3.00
  else:
    price_per_weight = 1.50
  return price_per_weight * weight + 20


def drone(weight): 
#   if weight >= 10:
#     drone_cost = 14.25 * weight
#     return drone_cost
#   elif weight >= 6:
#     drone_cost = 12.00 * weight
#     return drone_cost
#   elif weight >= 2:
#     drone_cost = 9.00 * weight
#     return drone_cost
#   else:
#     drone_cost = 4.50 * weight
#     return drone_cost
  if weight >= 10:
    price_per_weight = 14.25
  elif weight >= 6:
    price_per_weight = 12.00
  elif weight >= 2:
    price_per_weight = 9.00
  else:
    price_per_weight = 4.50
  return price_per_weight * weight

flat_charge = 125

def ship_method(weight):
  if ground(weight) < drone(weight) < flat_charge:
    cost = ground(weight)
    return "Ground is the cheapest method for $" + str(cost) + " dollars."
  elif drone(weight) < ground(weight) < flat_charge:
    cost = drone(weight)
    return "Drone is the cheapest method for $" + str(cost) + " dollars."
  else:
    cost = flat_charge
    return "Premium Ground is the cheapest method for $" + str(cost) + " dollars."

# testing
# print(ground(8.4))
# print(drone(1.5))

weight = 1.5
print(ship_method(weight))

weight = 4.8
print(ship_method(weight))

weight = 41.5
print(ship_method(weight))

def print_something(x):
  if x <= 2:
    print("This is printed")
  if x <= 4:
    print("This is also printed")
  if x <= 6:
    print("Is this printed?")
  if x <= 8:
    print("This might be printed.")

print_something(5)

def simple_conditional(x):
  if x == 0:
    print("x is equal to zero.")
  elif x >= 0:
    print("x is greater than zero.")
  else:
    print("x is less than zero.")

simple_conditional(0)