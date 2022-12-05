import sys
from re import search
from collections import Counter


class ShopItem:
    def __init__(self, name: str, weight: (int | float), price: (int | float)):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        return hash(self) == hash(other)


if __name__ == '__main__':
    # lst_in = list(map(str.strip, sys.stdin.readlines()))
    lst_in = ['Системный блок: 1500 75890.56',
              'Монитор Samsung: 2000 34000',
              'Клавиатура: 200.44 545',
              'Монитор Samsung: 2000 34000',
              ]
    pattern_str = r'([^:]+):\s+(\S+)\s+(\S+)'
    shop_list = []
    for line in lst_in:
        match = search(pattern_str, line)
        shop_list.append(ShopItem(match.group(1), float(match.group(2)), float(match.group(3))))
    shop_count = Counter(shop_list)
    shop_items = dict.fromkeys(shop_list)
    for item in shop_items:
        shop_items[item] = [item, shop_count[item]]

    it1 = ShopItem('name', 10, 11)
    it2 = ShopItem('name', 10, 11)
    assert hash(it1) == hash(it2), "разные хеши у равных объектов"

    it2 = ShopItem('name', 10, 12)
    assert hash(it1) != hash(it2), "равные хеши у разных объектов"

    it2 = ShopItem('name', 11, 11)
    assert hash(it1) != hash(it2), "равные хеши у разных объектов"

    it2 = ShopItem('NAME', 10, 11)
    assert hash(it1) == hash(it2), "разные хеши у равных объектов"

    name = lst_in[0].split(':')
    for sp in shop_items.values():
        assert isinstance(sp[0], ShopItem) and type(sp[
                                                        1]) == int, "в значениях словаря shop_items первый элемент должен быть объектом класса ShopItem, а второй - целым числом"

    v = list(shop_items.values())
    if v[0][0].name.strip() == "Системный блок":
        assert v[0][1] == 1 and v[1][1] == 2 and v[2][1] == 1 and len(v) == 3, "неверные значения в словаре shop_items"

    if v[0][0].name.strip() == "X-box":
        assert v[0][1] == 2 and v[1][1] == 1 and v[2][1] == 2 and len(v) == 3, "неверные значения в словаре shop_items"
