import unittest

from hashmap import HashMap


class TestHashMap(unittest.TestCase):
    def setUp(self):
        self.hashmap = HashMap(size=10)

    def test_put_and_get(self):
        self.hashmap.put(1, "cat")
        self.hashmap.put(2, "raccoon")

        self.assertEqual(self.hashmap.get(1), "cat")
        self.assertEqual(self.hashmap.get(2), "raccoon")
        self.assertIsNone(self.hashmap.get(3))

    def test_collision_handling(self):
        self.hashmap.put(1, "platypus")
        # This will cause a collision as 11 % 10 == 1
        self.hashmap.put(11, "kangaroo")

        self.assertEqual(self.hashmap.get(1), "platypus")
        self.assertEqual(self.hashmap.get(11), "kangaroo")

    def test_update_existing_key(self):
        self.hashmap.put(1, "cat")
        # Update the value for the existing key
        self.hashmap.put(1, "raccoon")

        self.assertEqual(self.hashmap.get(1), "raccoon")

    def test_non_existent_key(self):
        self.assertIsNone(self.hashmap.get(1))
        self.assertIsNone(self.hashmap.get(5))


if __name__ == "__main__":
    unittest.main()
