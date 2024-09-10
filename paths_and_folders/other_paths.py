from pathlib import Path

other_path = Path.home() / 'I' / 'dont' / 'exist.csv'

print(other_path)

if other_path.exists():
    with open(other_path, 'r') as file:
        print(file.read())
else:
    print('The file does not exist.')