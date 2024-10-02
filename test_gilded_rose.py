# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def test_conjured_quality_degrades_twice_as_fast(self):
        items = [Item("Conjured", 15, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 4)

    def test_conjured_quality_degrades_twice_as_fast_after_sell_date(self):
        items = [Item("Conjured", 0, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 2)

    def test_conjured_quality_never_negative(self):
        items = [Item("Conjured", 0, -2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertGreaterEqual(items[0].quality, 0)

if __name__ == '__main__':
    unittest.main()
