from Animal import Animal
import random


class Zoo():

    MEAT_PRICE = 4
    WEED_PRICE = 2
    TIME_PASSED = 0
    INCOME_FOR_ANIMAL = 60
    GENDERS = ["male", "female"]

    def __init__(self, animals, capacity, budget):
        self.animals = animals
        self.capacity = capacity
        self.budget = budget
        self.babies = []
        self.pregnants = []

    def accommodate_animal(self, animal):
        if self.capacity > len(self.animals):
            self.animals.append(animal)
            return True
        else:
            print ("Full capacity")
            return False

    def get_daily_incomes(self):
        incomes = 0
        for animal in self.animals:
            incomes += self.INCOME_FOR_ANIMAL
        return incomes

    def get_daily_outcomes(self):
        outcomes = 0
        for animal in self.animals:
            if animal.food_type == 'meat':
                self.budget -= self.MEAT_PRICE
                outcomes += self.MEAT_PRICE
            else:
                self.budget -= self.WEED_PRICE
                outcomes += self.WEED_PRICE
        return outcomes

    def animal_die(self, animal):
        alive_animals = self.animals
        for animal in self.animals:
            if not animal.is_alive:
                alive_animals.remove(animal)
        self.animals = alive_animals
        return self.animals

    def animal_reproduce(self):
        for i in range(0, len(self.animals)):
            for j in range(0, len(self.animals)):
                if (self.animals[i].gender == 'male' and self.animals[j].gender == 'female'
                    and self.animals[i].species == self.animals[j].species
                    and self.TIME_PASSED % 6 == 0 and
                        self.animals[i] not in self.pregnants):
                    animal = Animal("animal", -self.animals[i].gestation_period,
                                    random.choice(self.GENDERS),
                                    87, "species", 20, "carnivore", 9, 20, 100, 200, 20)
                    self.babies.append(animal)
                    self.pregnants.append(self.animals[j])
