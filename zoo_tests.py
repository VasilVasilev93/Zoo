import unittest
from zoo import Zoo
from Animal import Animal


class Test_Zoo(unittest.TestCase):

    def setUp(self):
        self.zoo = Zoo([], 10, 30)
        self.animal = Animal("name", 18, "male", 87, "species", 10, "meat", 9, 20, 100, 200, 20)
        self.animal1 = Animal("name1", 18, "female", 87, "species", 10, "meat", 9, 20, 100, 200, 20)
        self.zoo.accommodate_animal(self.animal)
        self.zoo.accommodate_animal(self.animal1)

    def test_init(self):
        self.assertEqual(self.zoo.animals, [self.animal, self.animal1])
        self.assertEqual(self.zoo.capacity, 10)
        self.assertEqual(self.zoo.budget, 30)

    def test_accommodate_animal(self):
        output = [self.animal, self.animal1]
        result = self.zoo.animals
        self.assertEqual(output, result)

    def test_daily_incomes(self):
        self.animal2 = Animal("name", 18, "male", 87, "species", 10, "meat", 9, 20, 100, 200, 20)
        output = 120
        result = self.zoo.get_daily_incomes()
        self.assertEqual(output, result)

    def test_daily_outcomes(self):
        output = 8
        result = self.zoo.get_daily_outcomes()
        self.assertEqual(output, result)

    def test_animal_die(self):
        output = [self.animal]
        result = self.zoo.animal_die(self.animal1)
        self.assertEqual(output, result)

    def test_reproduction(self):
        self.assertTrue(self.zoo.animal_reproduce(self.animal, self.animal1))

if __name__ == '__main__':
    unittest.main()