# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def test_vest_decreases_in_quality(self):
        items = [Item("+5 Dexterity Vest", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 9)

    def test_aged_brie_increases_in_quality(self):
        items = [Item("Aged Brie", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 11)

    def test_conjured_items_degrade_twice_as_fast(self):
        items = [Item("Conjured Mana Cake", 12, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 8)

if __name__ == '__main__':
    unittest.main()
