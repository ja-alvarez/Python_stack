class Zoo():
    def __init__(self, name, animals=[]):
        self.name = name
        self.animals = []
    def add_animal(self, animal_name):
        self.animals.append(animal_name)
        return self
    def print_animals(self):
        print(f"In {self.name}, we have these animals: ")
        for animal in self.animals:
            animal.display_info()

class Animal():
    def __init__(self, name, age, health_level, happiness_level):
        self.name = name
        self.age = age
        self.health_level = health_level
        self.happiness_level = happiness_level
    def feed_animal(self):
        self.health_level += 10
        self.happiness_level += 10
        return self

class Lion(Animal):
    def __init__(self, name, age, health_level, happiness_level):
        super().__init__(name, age, health_level, happiness_level)
        self.skill = "Roar"
    def display_info(self):
        print(f"{self.name} is at {self.health_level} health level and at {self.happiness_level} happiness level! My special skill is {self.skill}.")
        return self
    def feed_animal(self):
        self.health_level += 20
        self.happiness_level += 10
        return self


class Panda(Animal):
    def __init__(self, name, age, health_level, happiness_level):
        super().__init__(name, age, health_level, happiness_level)
        self.skill = "Headbutt"
    def display_info(self):
        print(f"{self.name} is at {self.health_level} health level and at {self.happiness_level} happiness level! My special skill is {self.skill}.")
        return self
    def feed_animal(self):
        super().feed_animal()
        return self

class Tiger(Animal):
    def __init__(self, name, age, health_level, happiness_level):
        super().__init__(name, age, health_level, happiness_level)
        self.skill = "Scratch"
    def display_info(self):
        print(f"{self.name} is at {self.health_level} health level and at {self.happiness_level} happiness level! My special skill is {self.skill}.")
        return self
    def feed_animal(self):
        super().feed_animal()
        return self

zoo1 = Zoo("Juan's Zoo")

nala = Lion("Nala", 5, 100, 100)
zoo1.add_animal(nala)
nala.feed_animal().feed_animal()

simba = Lion("Simba", 5, 100, 100)
zoo1.add_animal(simba)
simba.feed_animal().feed_animal()

po = Panda("Po", 2, 30, 30)
zoo1.add_animal(po)
po.feed_animal().feed_animal()

rajah = Tiger("Rajah", 1, 50, 50)
zoo1.add_animal(rajah)
rajah.feed_animal().feed_animal()

sherekhan = Tiger("Shere Khan", 1, 50, 50)
zoo1.add_animal(sherekhan)
sherekhan.feed_animal().feed_animal()


zoo1.print_animals()