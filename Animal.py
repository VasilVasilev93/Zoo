import random



class Animal:
    INITIAL_CHANCE_TO_DIE = 1

    def __init__(self, name, age, gender, weight, species, life_expectancy, food_type, gestation_period, newborn_weight, average_weight, weight_age_ratio, food_weight_ratio):
        self.is_alive = True
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight
        self.species = species
        self.life_expectancy = life_expectancy
        self.food_type = food_type
        self.gestation_period = gestation_period
        self.newborn_weight = newborn_weight
        self.average_weight = average_weight
        self.weight_age_ratio = weight_age_ratio
        self.food_weight_ratio = food_weight_ratio
        self.chance_to_die = self.INITIAL_CHANCE_TO_DIE
        self.pregnancy_ban = 0

    def grow(self):
        if self.is_alive:
            self.age += 1 / 365
            self.weight += 1
            self.chance_to_die = self.age / (self.life_expectancy * 100 * 365)
            chance = random.randint(0, 100)
            if chance < self.chance_to_die:
                print(self.age)
                print (self.chance_to_die, chance)
                self.is_alive = False

    def eat(self, food_weight):
        self.weight += food_weight

    def __str__(self):
        return self.name
