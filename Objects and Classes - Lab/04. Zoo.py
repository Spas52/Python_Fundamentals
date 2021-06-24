class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.bird = []

    def add_animal(self, race, name):
        if race == "mammal":
            self.mammals.append(name)
        elif race == "fish":
            self.fishes.append(name)
        elif race == "bird":
            self.bird.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            return f"Mammals in {self.name}: {', '.join(self.mammals)}\nTotal animals: {Zoo.__animals}"
        elif species == "fish":
            return f"Fishes in {self.name}: {', '.join(self.fishes)}\nTotal animals: {Zoo.__animals}"
        elif species == "bird":
            return f"Birds in {self.name}: {', '.join(self.bird)}\nTotal animals: {Zoo.__animals}"


zoo_name = input()
zoo = Zoo(zoo_name)
n = int(input())

for animal in range(n):
    name_of_animal = input().split(" ")
    species = name_of_animal[0]
    name = name_of_animal[1]
    zoo.add_animal(species, name)

info = input()
print(zoo.get_info(info))
