from Animal import Animal
import random


class Zoo():

    MEAT_PRICE = 4
    WEED_PRICE = 2
    TIME_PASSED = 0
    INCOME_FOR_ANIMAL = 60
    FOOD_DAY_DOSE = 5
    GENDERS = ["male", "female"]

    def __init__(self, animals, capacity, budget):
        self.animals = animals
        self.capacity = capacity
        self.budget = budget
        self.babies = []
        self.pregnants = []
        self.grave_yard = []

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
                outcomes += self.MEAT_PRICE
            else:
                outcomes += self.WEED_PRICE
        return outcomes

    def animal_die(self):
        grave_yard = []
        alive_animals = self.animals
        for animal in self.animals:
            if not animal.is_alive:
                grave_yard.append(animal)
                self.grave_yard.append(animal)
                alive_animals.remove(animal)
        self.animals = alive_animals
        return grave_yard

    def move_to_habitat(self, species, name):
        for animal in self.animals:
            if animal.species == species and animal.name == name:
                self.animals.remove(animal)
                break

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

    def get_new_born_animals(self):
        new_borns = []
        for animal in self.babies:
            if animal.age == -6:
                new_borns.append(animal)
        return new_borns

    def animals_are_going_to_die(self):
        animals_going_to_die = []
        for animal in self.animals:
            if animal.life_expectancy - animal.age < 2:
                animals_going_to_die.append(animal)
        return animals_going_to_die

    def see_animals(self):
        for animal in self.animals:
            print("{} : {}, {}, {}".format(animal.name, animal.species, animal.age, animal.weight))

    def print_grave_yard(self):
        if self.grave_yard != []:
            print("Dead animals: ")
            for animal in self.grave_yard:
                print("{} : {}".format(animal.name, animal.species))



    def simulate(self, interval_of_time, period):
        if period == "weeks":
            period /= 7
        elif period == "months":
            period /= 30
        while period >= 0:
            for animal, baby in zip(self.animals, self.babies):
                animal.eat(self.FOOD_DAY_DOSE)
                animal.grow()
                baby.grow()
            animals_going_to_die = self.animals_are_going_to_die()
            if animals_going_to_die != []:
                print("These animals are going to die: ", "  ".join(animals_going_to_die))
            dead_animals = self.dead_animals()
            if dead_animals != []:
                print("Dead animals today : ", "  ".join(dead_animals))
            self.budget += self.get_daily_incomes
            self.budget -= self.get_daily_outcomes
            if self.budget < 0:
                print("Dont have enought money to feed all animals !!!")
                break
            new_borns = self.get_new_born_animals()
            if new_borns != []:
                print("Animals conceived today : ", "  ".join(new_borns))
            self.animal_reproduce()
        self.see_animals()
        self.print_grave_yard()





