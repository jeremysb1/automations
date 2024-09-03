import csv

def rating_category(rating):
    if rating <= -3:
        category = 'abysmal'
    elif rating <= -1:
        category = 'awful'
    else:
        category = 'bad'
    
    return category

modified_dad_jokes = []

with open('dad_jokes.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    headers = next(csv_reader)
    headers.append('rating_category')

    for row in csv_reader:
        rating_category(row[2])