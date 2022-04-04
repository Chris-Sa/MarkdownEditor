# read animals.txt
# and write animals_new.txt

animals = open("animals.txt", "r")
new_animals = open("animals_new.txt", 'w')
for line in animals:
    data = line.replace("\n", " ")
    new_animals.write(data)

animals.close()
new_animals.close()