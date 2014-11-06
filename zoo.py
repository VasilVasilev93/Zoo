from Animal import Animal
import random


class Zoo():

    MEAT_PRICE = 4
    WEED_PRICE = 2
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

    def animal_die(self, animals_close_to_death):
        grave_yard = []
        alive_animals = self.animals
        for animal in animals_close_to_death:
            if not animal.is_alive:
                grave_yard.append(animal.name)
                self.grave_yard.append(animal)
                animals_close_to_death.remove(animal)
                alive_animals.remove(animal)
        self.animals = alive_animals
        return grave_yard

    def _are_different_genders(self, animal1_gender, animal2_gender):
        if animal1_gender == 'female':
            return animal1_gender != animal2_gender
        return False

    def _is_time_to_reproduce(self, animal1, animal2):
        animal1_ban = animal1.reproduce_ban
        animal2_ban = animal2.reproduce_ban
        if animal1.gender == 'female' and animal1_ban <= 0 and animal2_ban <= 0:
            return True
        return False

    def _is_female_animal_pregnant(self, animal1):
        if animal1 not in self.pregnants and animal1.gender == 'female':
            return True
        return False

    def _has_pregnancy_ban_passed(self, animal1):
        if animal1.gender == 'female' and animal1.pregnancy_ban <= 0:
            animal1.pregnancy_ban = 0
            return True
        return False

    def _is_ready_to_reproduce(self, animal1, animal2):
        if not self._are_different_genders(animal1.gender, animal2.gender):
            #print ("FAIL genders")
            return False
        if not self._is_time_to_reproduce(animal1, animal2):
            #print ("FAIL time to reproduce")
            return False
        if not self._is_female_animal_pregnant(animal1):
            #print ("FAIL pregnant")
            return False
        if not self._has_pregnancy_ban_passed(animal1):
            #print ("FAIL pregnancy ban")
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
                    animal1.reproduce_ban = 6
                    animal2.reproduce_ban = 6
                    baby_gest_period = -animal1.gestation_period
                    baby_gender = random.choice(self.GENDERS)
                    baby_species = animal1.species
                    baby = Animal("bebe", baby_gest_period,
                                  baby_gender, 87, baby_species, 100,
                                  "carnivore", 9, 20, 100, 200, 20)
                    self.babies.append(baby)
                    self.pregnants.append(animal1)
                    print (baby.name)
                    return True
        return False

    def baby_born(self):
        for baby in self.babies:
            if baby.age >= 0:
                for mother in self.pregnants:
                    #print ("mother when she got pregnant: ", mother.age - mother.gestation_period)
                    #print ("baby sasdas: ", mother.age - baby.age)
                    if mother.age - mother.gestation_period == mother.age - baby.age:
                       # print ("NOOOOO")
                        mother.pregnancy_ban += mother.gestation_period
                        self.pregnants.remove(mother)
                self.animals.append(baby)
                self.babies.remove(baby)

    def get_new_born_animals(self):
        new_borns = []
        for animal in self.babies:
            if animal.age == 0:
                new_borns.append(animal)
        return new_borns

    def animals_close_to_death(self):
        animals_going_to_die = []
        for animal in self.animals:
            if animal._is_close_to_death(animal.age):
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

    def simulate(self, period, interval_of_time):
        count = 0
        period = int(period)
        if interval_of_time == "weeks":
            period *= 7
        elif interval_of_time == "months":
            period *= 30
        elif interval_of_time == "years":
            period *= 365
        while period > 0:
            count += 1
            self.animal_reproduce()
            self.baby_born()
            #print (self.pregnants)
            #print (self.babies)
            for animal in self.animals:
                animal.eat(self.FOOD_DAY_DOSE)

                animal.pregnancy_ban -= 1/30

                if animal.pregnancy_ban > 0:
                    animal.pregnancy_ban -= 0.033
                    if animal.pregnancy_ban < 0:
                        animal.pregnancy_ban = 0
                if animal.reproduce_ban > 0:
                    animal.reproduce_ban -= 0.033
                    if animal.reproduce_ban < 0:
                        animal.reproduce_ban = 0

                animal.grow()

            for baby in self.babies:
                baby.grow()

            animals_going_to_die = self.animals_close_to_death()
            animals_names_close_to_death = []
            for animal in animals_going_to_die:
                animals_names_close_to_death.append(animal.name)
            if animals_going_to_die != []:
                print("These animals are likely to die soon: ", "  ".join(animals_names_close_to_death))

            dead_animals = self.animal_die(animals_going_to_die)
            if dead_animals != []:
                print("Dead animals today : ", "  ".join(dead_animals))
            self.budget += self.get_daily_incomes()
            self.budget -= self.get_daily_outcomes()
            if self.budget < 0:
                print("Dont have enought money to feed all animals !!!")
                break
            new_borns = self.get_new_born_animals()
            if new_borns != []:
                print("Animals conceived today : ", "  ".join(new_borns))

            self.animal_reproduce()
            period -= 1/30


            period -= 1

        self.see_animals()
        self.print_grave_yard()


def main():
    animal1 = Animal("name", 18, "male", 87, "species", 100, "carnivore", 3, 20, 100, 200, 20)
    animal2 = Animal("animal", 18, "male", 87, "panda", 100, "carnivore", 3, 20, 100, 200, 20)
    animal3 = Animal("animal3", 18, "female", 87, "panda", 100, "carnivore", 3, 20, 100, 200, 20)
    animal4 = Animal("animal4", 18, "female", 87, "species", 100, "carnivore", 3, 20, 100, 200, 20)
    animals = [animal1, animal2, animal3, animal4]
    zoo = Zoo(animals, 20, 1000)
    command = ""
    while(command != "exit"):
        command = input("enter command:")
        if command == "see_animals":
            zoo.see_animals()
        else:
            command = command.split(" ")
            if command[0] == "accommodate":
                animal = Animal(command[2], int(command[3]), None, int(
                    command[4]), command[1], None, None, None, None, None, None, None,)
                zoo.accommodate_animal(animal)
            elif command[0] == "move_to_habitat":
                zoo.move_to_habitat(command[1], command[2])
            elif command[0] == "simulate":
                zoo.simulate(command[1], command[2])


if __name__ == '__main__':
    main()
