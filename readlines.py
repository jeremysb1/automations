file = open('dad_jokes.txt', 'r')
lines = file.readlines()

for line in lines:
    print(line.strip())