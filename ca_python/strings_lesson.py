def letter_check(word,letter):
  for i in word:
    if i == letter:
      return True
  return False

print(letter_check("strawberry","a"))

