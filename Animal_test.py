import unittest
from Animal import Animal


class TestAnimal(unittest.TestCase):

    def setUp(self):
        self.animal = Animal("name", 18, "male", 87, "species", 10, "carnivore", 9, 20, 100, 200, 20)

    def test_animal_init(self):
        self.assertEqual(self.animal.name, "name")
        self.assertEqual(self.animal.age, 18)
        self.assertEqual(self.animal.gender, "male")
        self.assertEqual(self.animal.weight, 87)
        self.assertEqual(self.animal.species, "species")
        self.assertEqual(self.animal.life_expectancy, 10)
        self.assertEqual(self.animal.food_type, "carnivore")
        self.assertEqual(self.animal.gestation_period, 9)
        self.assertEqual(self.animal.newborn_weight, 20)
        self.assertEqual(self.animal.average_weight, 100)
        self.assertEqual(self.animal.weight_age_ratio, 200)
        self.assertEqual(self.animal.food_weight_ratio, 20)
        self.assertTrue(self.animal.is_alive)

    def test_animal_grow(self):
        self.animal.grow()
        self.assertEqual(self.animal.age, 18.033)
        self.assertEqual(self.animal.weight, 88)

    def test_animal_eat(self):
        self.animal.eat(10)
        self.assertEqual(self.animal.weight, 97)

    def test_animal_die(self):
        results = set()
        for i in range(1000):
            self.animal.grow()
            results.add(self.animal.is_alive)
        self.assertTrue(True in results)

if __name__ == '__main__':
    unittest.main()
