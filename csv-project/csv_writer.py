import csv

with open('expensive_pets.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)

    csv_writer.writerow(['name', 'species', 'favorite_snack', 'monthly_cost'])
    csv_writer.writerow(['Buddy', 'dog', 'sliders', 1000])

    csv_writer.writerows([
        ['Daisy', 'dog', 'jerky', 500],
        ['Rex', 'dog', 'bones', 300],
        ['Pepper', 'dog', 'cheese', 100]
    ])