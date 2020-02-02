import csv

isbn_list = []
with open('books.csv') as books_csv:
  books_reader = csv.DictReader(books_csv, delimiter='@')
  for row in books_reader:
    isbn_list.append(row['ISBN'])

