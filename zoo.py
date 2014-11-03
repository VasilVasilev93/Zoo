class Zoo():

    MEAT_PRICE = 4
    WEED_PRICE = 2

    INCOME_FOR_ANIMAL = 60

    def __init__(self, animals, capacity, budget):
        self.animals = animals
        self.capacity = capacity
        self.budget = budget

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
        # for animal in self.animals:
        #     if not animal.is_alive:
        alive_animals.remove(animal)
        self.animals = alive_animals
        return self.animals

    def animal_reproduce(self, male, female):
        if female.gender == female and male.gender == male:
            return True
        return False


