# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class ItemStrategy:
    def update(self, item: Item):
        raise NotImplementedError("This method should be overridden by subclasses")

class NormalItemStrategy(ItemStrategy):
    def update(self, item: Item):
        if item.quality > 0:
            item.quality -= 1
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 1

class AgedBrieStrategy(ItemStrategy):
    def update(self, item: Item):
        if item.quality < 50:
            item.quality += 1
        item.sell_in -= 1

class BackstagePassesStrategy(ItemStrategy):
    def update(self, item: Item):
        if item.quality < 50:
            item.quality += 1
            if item.sell_in < 11 and item.quality < 50:
                item.quality += 1
            if item.sell_in < 6 and item.quality < 50:
                item.quality += 1
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0

class SulfurasStrategy(ItemStrategy):
    def update(self, item: Item):
        # doesn't decrease in quality or sell_in
        pass

class VestStrategy(ItemStrategy):
    def update(self, item: Item):
        if item.quality > 0:
            item.quality -= 1
        item.sell_in -= 1

class ConjuredItemStrategy(ItemStrategy):
    def update(self, item: Item):
        if item.quality > 0:
            item.quality -= 2
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 2

class GildedRose:

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            strategy = self.get_strategy(item)
            strategy.update(item)

    def get_strategy(self, item: Item) -> ItemStrategy:
        if item.name == "Aged Brie":
            return AgedBrieStrategy()
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePassesStrategy()
        elif item.name == "Sulfuras, Hand of Ragnaros":
            return SulfurasStrategy()
        elif item.name == "Conjured Mana Cake":
            return ConjuredItemStrategy()
        elif item.name == '+5 Dexterity Vest':
            return VestStrategy()
        else:
            return NormalItemStrategy()
