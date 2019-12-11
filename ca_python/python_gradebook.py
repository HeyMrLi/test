last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

# new grades
subjects.append("computer science")
grades.append(100)

gradebook = list(zip(subjects, grades))
gradebook.append(("visual arts", 93))

print("This semester's gradebook: " + str(list(gradebook)))
print("-" * 40)
full_gradebook = gradebook + last_semester_gradebook
print("Full year's gradebook: " + str(full_gradebook))

# Testing len() function and index values.
examples = ['red', 'green', 'blue', 'orange']

# This will print 4 which is the number of elements in examples.
print(len(examples))

# This will return a list ([0, 1, 2, 3]) which provides indexes to the examples.
for color in range(len(examples)):
   print(examples[color])

from random import randint

elements = ['Hydrogen', 'Helium', 'Carbon', 'Oxygen', 'Nitrogen']

for count in range(10):
    index = randint(0, len(elements) - 1)
    print(elements[index])
    