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

    def _are_different_genders(self, animal1_gender, animal2_gender):
        if animal1_gender == 'female':
            return animal1_gender != animal2_gender
        return False

    def _is_time_to_reproduce(self, animal1, animal2):
        if animal1.gender == 'female':
            animal1_time = animal1.age % self.REPRODUCE_PERIOD
            animal2_time = animal2.age % self.REPRODUCE_PERIOD
        if animal1_time == 0 and animal2_time == 0:
            return True
        return False

    def _is_some_animal_pregnant(self, animal1, animal2):
        if animal1 not in self.pregnants or animal2 not in self.pregnants:
            return True
        return False

    def _has_pregnancy_ban_passed(self, animal1):
        if animal1.gender == 'female' and animal1.pregnancy_ban <= 0:
            return True
        return False

    def _is_ready_to_reproduce(self, animal1, animal2):
        if not self._are_different_genders(animal1.gender, animal2.gender):
            return False
        if not self._is_time_to_reproduce(animal1, animal2):
            return False
        if not self._is_some_animal_pregnant(animal1, animal2):
            return False
        if not self._has_pregnancy_ban_passed(animal1):
            return False
        return True

    def move_to_habitat(self, species, name):
        for animal in self.animals:
            if animal.species == species and animal.name == name:
                self.animals.remove(animal)
                break

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
                    return True
        return False

    def baby_born(self):
        for baby in self.babies:
            if baby.age == 0:
                for mother in self.pregnants:
                    if mother.age == mother.age + mother.gestation_period:
                        mother.pregnancy_ban += mother.gestation_period
                        self.pregnants.remove(mother)
                self.animals.append(baby)
                self.babies.remove(baby)

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
            for animal in self.animals:
                animal.eat(self.FOOD_DAY_DOSE)
                animal.pregnancy_ban -= 0.033
                animal.grow()
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
