with open('welcome.txt') as text_file:
  text_data = text_file.read()
print(text_data)

with open('how_many_lines.txt') as lines_doc:
  line = lines_doc.read()
print(line)

with open('how_many_lines.txt') as lines_doc:
  for line in lines_doc.readlines():
    print(line)

with open('just_the_first.txt') as first_line_doc:
  first_line = first_line_doc.readline()
  print(first_line)
  second_line = first_line_doc.readline()
  print(second_line)