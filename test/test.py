import unittest
import sys

sys.path.append('..')

import generator

class TestSuite(unittest.TestCase):
    def test_get_random_word_success(self):
        self.assertTrue(len(generator.getRandomWord('noun', generator.API_KEY)) != 0)
    def test_get_random_word_fail(self):
        self.assertRaises(KeyError, generator.getRandomWord, "foobar", "foobar")
    def test_number_of_archetypes(self):
        self.assertEquals(len(generator.ARCHETYPES), 12)
    def test_archetype_coverage(self):
        names = () 
        for function in generator.ARCHETYPES:
            names += (function(generator.API_KEY),)
        self.assertEquals(len(names), 12)
    def test_function_integrity(self):
        passing = True
        names = ()
        for function in generator.ARCHETYPES:
            name = function(generator.API_KEY)
            if(len(name) == 0 or "  " in name):
               passing = False
        self.assertTrue(passing)

if __name__ == '__main__':
    unittest.main();
