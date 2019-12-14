
# # Write a function that returns the total number of unique letters in the string.

# letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# # Write your unique_english_letters function here:
# def unique_english_letters(word):
#   unique = [] ## Pretty happy with my code compared to the CodeAcademy solution below
#   for i in word:
#     if i not in unique:
#       unique.append(i)
#   count = 0
#   for letter in unique:
#       count += 1
#   return count

# # CodeAcademy Solution
# #     uniques = 0  
# #   for letter in letters: ## Their solution is dependent on the letters string whereas my solution is more self-contained
# #     if letter in word:
# #       uniques += 1
# #   return uniques

# # Uncomment these function calls to test your function:
# print(unique_english_letters("mississippi"))
# # should print 4
# print(unique_english_letters("Apple"))
# # should print 4

n = 5
arr = [2,3,6,6,5]

# // STRUGGLES
# print(arr)
# arr.sort()
# print(arr[n-1])

# print(len(arr))
# print(arr[4])
# for n in range(len(arr)):
#   unique = []
#   if n < (len(arr)-1) and arr[n] < arr[n+1]:
#     unique.append(arr[n])
# // END STRUGGLES

unique = []
for x in arr:
  if x not in unique:
    unique.append(x)

unique.sort()
print(unique[-2])
print("-" * 20)
print("-" * 20)


# Write your count_char_x function here:
def count_char_x(word,x):
  count = 0
  for i in word:
    if i == x:
      count += 1
  return count

# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1


# Write your count_multi_char_x function here:
def count_multi_char_x(word,x):
  splits = word.split(x)
  return(len(splits)-1) ## If I use print, it will return response and give None
  
# Uncomment these function calls to test your function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1


# // STRUGGLED ON THIS LOGICALLY
# Write your substring_between_letters function here:
def substring_between_letters(word,start,end):
  start_ind = word.find(start)
  end_ind = word.find(end)
  if start_ind == -1 or end_ind == -1:
    return word
  else:
    return word[start_ind+1:end_ind]

# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"
# // STRUGGLED ON THIS LOGICALLY


# // RELATIVELY EASY
# Write your x_length_words function here:
def x_length_words(sentence,x):
  split_sent = sentence.split()
  for word in split_sent:
    if len(word) >= x:
      return True
    return False
    
# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True


# Write your check_for_name function here:
def check_for_name(sentence,name):
#   lowercase_name = name.lower()
#   lower_split_sent = sentence.lower().split()
#   for x in lower_split_sent:
#     if lowercase_name == x:
#       return True
#   return False
  return name.lower() in sentence.lower() ## WOW... SO SIMPLE


# Uncomment these function calls to test your  function:
# print(check_for_name("My name is Jamie", "Jamie"))
# should print True
#print(check_for_name("My name is jamie", "Jamie"))
# should print True
#print(check_for_name("My name is Samantha", "Jamie"))
# should print False


# // This was VERY INTUITIVE for me
# Write your every_other_letter function here:
def every_other_letter(word):
  return word[::2]

# Uncomment these function calls to test your function:
#print(every_other_letter("Codecademy"))
# should print Cdcdm
#print(every_other_letter("Hello world!"))
# should print Hlowrd
#print(every_other_letter(""))
# should print 


# Write your reverse_string function here:
def reverse_string(word):
  return word[::-1] ## INGENIOUS!

# Uncomment these function calls to test your  function:
#print(reverse_string("Codecademy"))
# should print ymedacedoC
#print(reverse_string("Hello world!"))
# should print !dlrow olleH
#print(reverse_string(""))
# should print


# Write your make_spoonerism function here:
def make_spoonerism(word1, word2):
  redac_word1 = word2[0] + word1[1:]
  redac_word2 = word1[0] + word2[1:]
  return redac_word1 + " " + redac_word2

# Uncomment these function calls to test your function:
#print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
#print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
#print(make_spoonerism("a", "b"))
# should print b a


# Write your add_exclamation function here:
def add_exclamation(word):
  while len(word) < 20:
    word = word + "!"
  else:
    return word

# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn