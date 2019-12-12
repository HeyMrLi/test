board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']

sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']

for game in board_games:
  print(game)
print("-" * 20)
for x in sport_games:
  print(x)

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for age in ages:
  if age < 21:
    continue
  print(age)

all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

while len(students_in_poetry) < 6:
  students_in_poetry.append(all_students.pop())

print(students_in_poetry)

for x in range(5):
    for y in range(5):
        print("X ",end='')
    print()

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [height for height in heights if height > 161]

# can_ride_coaster = []
# for height in heights:
#   if height > 161:
#     can_ride_coaster.append(height)

print(can_ride_coaster)

celsius = [0, 10, 15, 32, -5, 27, 3]
fahrenheit = [temp_c * (9 / 5) + 32 for temp_c in celsius]

print(fahrenheit)