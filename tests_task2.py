import unittest
from task2 import damage


class TestCases(unittest.TestCase):
    def testSpells(self):
        spell_points = {'feeai': 2, 'feaineain': 7, 'jee': 0, 'fefefefefeaiaiaiaiai': 0, 'fdafafeajain': 1,
                        'fexxxxxxxxxxai': 0, 'fedaineai': 10, 'jejeai': 0, 'jejefeai': 3, 'dadsafeokokok': 0,
                        'aioooofe': 0}
        # dict of some spells and their damage points
        for i, spell in enumerate(spell_points.keys()):
            with self.subTest(spell=spell):
                self.assertEqual(damage(spell), spell_points[spell])
                # test if function damage() calculates damage points properly

if __name__ == "__main__":
    unittest.main()
