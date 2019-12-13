def letter_check(word,letter):
  for i in word:
    if i == letter:
      return True
  return False

print(letter_check("strawberry","a"))

def contains(big_string,little_string):
  if little_string in big_string:
    return True
  return False

print(contains("watermelon","melon"))
print(contains("watermelon","berry"))

# def common_letters(string_one,string_two):
#   for i in range(len(string_one)):
#     for i2 in range(len(string_two)):
#       if string_one[i] == string_two[i2]:
#         return string_one[i]
        
# print(common_letters('manhattan', 'san francisco'))

def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return common

print(common_letters('manhattan', 'san francisco'))

def username_generator(first,last):
    user_name = []
    if len(first) >= 3:
        user_name = first[:3]
    else:
        user_name = first
    if len(last) >= 4:
        user_name += last[:4]
    else:
        user_name += last
    return user_name

print(username_generator("Abe","Simpson"))

def password_generator(user_name):
    password = ""
    for i in range(len(user_name)):
        password += user_name[i-1]
    return password

# Challenging for me
print(password_generator(username_generator("Abe","Simpson")))

authors = "Audre Lorde, William Carlos Williams, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kamala Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni"

author_names = authors.split(",")
print(author_names)
print("-" * 20)
print(len(author_names))

author_last_names = []
for i in author_names:
  author_last_names.append(i.split()[-1])

print(author_last_names)

spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split('\n')
for i in range(len(spring_storm_lines)):
  print(spring_storm_lines[i])

winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = '\n'.join(winter_trees_lines)
print(winter_trees_full)

love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = []
for lst in love_maybe_lines:
  if not lst:
    continue
  else:
    love_maybe_lines_stripped.append(lst.strip())

print(love_maybe_lines_stripped)
print("-" * 20)
love_maybe_full = '\n'.join(love_maybe_lines_stripped)

print(love_maybe_full)

def poem_title_card(poet,title):
  return "The poem \"{}\" is written by {}.".format(title,poet)

print(poem_title_card("Walt Whitman", "I Hear America Singing"))

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

highlighted_poems_list = highlighted_poems.split(',')

highlighted_poems_stripped = []
for lst in highlighted_poems_list:
  highlighted_poems_stripped.append(lst.strip())
  
# print(highlighted_poems_stripped)

highlighted_poems_details = []
for poem in highlighted_poems_stripped:
  highlighted_poems_details.append(poem.split(':'))
  
titles = []
poets = []
dates = []

# print(highlighted_poems_details)
for detail in highlighted_poems_details:
  titles.append(detail[0]) 
  poets.append(detail[1])
  dates.append(detail[2])

print("Titles: \n" + str(titles))
print("Poets: \n" + str(poets))
print("Dates: \n" + str(dates))
print('-' * 20)

for i in range(len(highlighted_poems_details)):
  print("The poem {title} was published by {poet} in {date}.".format(title=titles[i],poet=poets[i],date=dates[i]))