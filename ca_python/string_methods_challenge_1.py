
# Write a function that returns the total number of unique letters in the string.

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def unique_english_letters(word):
  unique = [] ## Pretty happy with my code compared to the CodeAcademy solution below
  for i in word:
    if i not in unique:
      unique.append(i)
  count = 0
  for letter in unique:
      count += 1
  return count

# CodeAcademy Solution
#     uniques = 0  
#   for letter in letters: ## Their solution is dependent on the letters string whereas my solution is more self-contained
#     if letter in word:
#       uniques += 1
#   return uniques

# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4

