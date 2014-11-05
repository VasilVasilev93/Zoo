from Animal import Animal
import random


class Zoo():

    MEAT_PRICE = 4
    WEED_PRICE = 2
    TIME_PASSED = 0
    INCOME_FOR_ANIMAL = 60
    FOOD_DAY_DOSE = 5
    GENDERS = ["male", "female"]
    REPRODUCE_PERIOD = 6

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

    def _are_different_genders(self, animal1_gender, animal2_gender):
        if animal1_gender == 'female':
            return animal1_gender != animal2_gender
        return False

    def _is_time_to_reproduce(self, animal1_age, animal2_age):
        if animal1.gender == 'female':
            animal1_time = animal1_age % self.REPRODUCE_PERIOD
            animal2_time = animal1_age % self.REPRODUCE_PERIOD
        if animal1_time == 0 and animal2_time == 0:
            return True
        return False

    def _is_some_animal_pregnant(self, animal1, animal2):
        if animal1 not in self.pregnants or animal2 not in self.pregnants:
            return True
        return False

    def _is_ready_to_reproduce(self, animal1, animal2):
        if not self._are_different_genders(animal1.gender, animal2.gender):
            return False
        if not self._is_time_to_reproduce(animal1.age, animal2.age):
            return False
        if not self._is_some_animal_pregnant(animal1, animal2):
            return False
        return True

    def animal_reproduce(self):
        for i in range(0, len(self.animals)):
            for j in range(0, len(self.animals)):
                animal1 = self.animals[i]
                animal2 = self.animals[j]
                if self._is_ready_to_reproduce(animal1, animal2):
                    baby_gest_period = -animal1.gestation_period
                    baby_gender = random.choice(self.GENDERS)
                    baby_species = animal1.species
                    animal = Animal("animal", baby_gest_period,
                                    baby_gender, 87, baby_species, 20,
                                    "carnivore", 9, 20, 100, 200, 20)
                    self.babies.append(animal)
                    self.pregnants.append(animal1)

    def baby_born(self):
        for baby in self.babies:
            if baby.age == 0:
                for mother in self.pregnants:
                    if mother.age == mother.age + 6:
                        #todo -2months mother's age
                        self.pregnants.remove(mother)
                self.animals.append(baby)
                self.babies.remove(baby)

    def simulate(self, interval_of_time, period):
        if period == "weeks":
            period /= 7
        elif period == "months":
            period /= 30
        while period >= 0:
            for animal in self.animals:
                animal.eat(self.FOOD_DAY_DOSE)
                animal.grow()
                self.animal_die(animal)
            self.animal_reproduce()
