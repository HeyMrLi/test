def get_boundaries(target,margin):
  low_limit = target - margin
  high_limit = margin + target
  return low_limit, high_limit

low, high = get_boundaries(100,20)

print(low,high)

current_year = 2048

def calculate_age(birth_year):
  age = current_year - birth_year
  return age
  
print(current_year)
print(calculate_age(1970))

def repeat_stuff(stuff,num_repeats=10):
    return stuff*num_repeats

lyrics = repeat_stuff("Row ",3) + "Your Boat. "
song = repeat_stuff(lyrics)
print(song)

# Physics Class

def f_to_c(f_temp):
    #Temp (C) = (Temp (F) - 32) * 5/9
    c_temp = (f_temp - 32) * 5/9
    return c_temp

print(f_to_c(100))

def c_to_f(c_temp):
    f_temp = c_temp * 5/9 + 32
    return f_temp

print(c_to_f(0))

train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

def get_force(mass,acceleration):
  return mass * acceleration
  
train_force = get_force(train_mass,train_acceleration)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

def get_energy(mass,c=3*10**8):
  return (mass * c) ** 2

bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

def get_work(mass,acceleration,distance):
    force = get_force(mass,acceleration)
    return force * distance

train_work = get_work(train_mass,train_acceleration,train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")

# Write your average function here:

def average(num1,num2):
  return (num1 + num2) / 2

# Uncomment these function calls to test your average function:
print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0

def multiples(num, multiple):
    for x in range(1, multiple + 1):
        print(num * x)
    return num * multiple

def dog_years(name,age):
  return "{name}, you are {dog_age} years old in dog years".format(name=name, dog_age=(age * 7))