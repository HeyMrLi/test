# drinks = ["espresso", "chai", "decaf", "drip"]
# caffeine = [64, 40, 0, 120]

# zipped_drinks = zip(drinks, caffeine)

# drinks_to_caffeine = {key:value for key, value in zipped_drinks}

# print(drinks_to_caffeine)

# songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
# playcounts = [78, 29, 44, 21, 89, 5]

# plays = {key:value for key, value in zip(songs, playcounts)}
# # print(plays)

# plays.update({"Purple Haze": 1})
# plays["Respect"] = 94
# print(plays)


# available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
# health_points = 20

# health_points += available_items.pop("stamina grains", 0)
# health_points += available_items.pop("power stew", 0)
# health_points += available_items.pop("mystic bread", 0)
# print(available_items, health_points)

# user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
# num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

# users = user_ids.keys()
# lessons = num_exercises.keys()
# print(users, lessons)

# pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

# for role, percent in pct_women_in_occupation.items():
#   print("Women make up " + str(percent) + " percent of " + role + "s.")

tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

spread = {}
spread.update({"past": tarot.pop(13)})
spread.update({"present": tarot.pop(22)})
spread.update({"future": tarot.pop(10)})

for time, card in spread.items():
  print("Your " + time + " is the " + card + " card.")

# Write your values_that_are_keys function here:
def values_that_are_keys(my_dictionary):
  matches = [] ## made a mistake here using curly brackets - need to define empty list not empty dictionary
  for value in my_dictionary.values():
    if value in my_dictionary.keys():
      matches.append(value)
  return matches

# Uncomment these function calls to test your  function:
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]

# Write your max_key function here:
def max_key(my_dictionary):
  largest_key = 0
  largest_value = 0
  for key, value in my_dictionary.items():
    if value > largest_value:
      largest_value = value
      largest_key = key
  return largest_key

# Uncomment these function calls to test your  function:
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"

# Write your word_length_dictionary function here:
def word_length_dictionary(words):
  word_length = {}
  for word in words:
    word_length[word] = len(word)
  return word_length

# Uncomment these function calls to test your  function:
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}

# Write your frequency_dictionary function here:
def frequency_dictionary(words):
  word_count = {}
  for word in words:
    if word not in word_count:
      word_count[word] = 0
    word_count[word] += 1
  return word_count

# Uncomment these function calls to test your  function:
#print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
#print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}

# Write your unique_values function here:
def unique_values(my_dictionary):
  count = []
  for value in my_dictionary.values():
    if value not in count:
      count.append(value)
  return len(count)

# Uncomment these function calls to test your  function:
#print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
#print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1


# Write your count_first_letter function here:
def count_first_letter(names):
  initials = {}
  for key in names:
    first = key[0]
    if first not in initials:
      initials[first] = 0
    initials[first] += len(names[key]) ## THIS IS CHALLENGING TO THINK ABOUT... WHY DOES THIS EXECUTE FOR THE FIRST KEY WHEN IT'S AN ELSE STATEMENT? WHy doesn't it skip this and go to the second key and start count there?
  return initials

# def count_first_letter(names):
#   letters = {}
#   for key in names:
#     first_letter = key[0]
#     if first_letter not in letters:
#       letters[first_letter] = 0
#     letters[first_letter] += len(names[key])
#   return letters

# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
#print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}