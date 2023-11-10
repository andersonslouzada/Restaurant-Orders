import csv
from typing import Set
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes: Set[Dish] = set()
        self._read_data(source_path)

    def _read_data(self, source_path: str) -> None:
        with open(source_path, "r") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)

            for row in csv_reader:
                d_name, d_price, i_name, i_quantity = (row)

                dish = next((d for d in self.dishes if d.name == d_name), None)
                if not dish:
                    dish = Dish(d_name, float(d_price))
                    self.dishes.add(dish)

                ingredient = Ingredient(i_name)
                dish.add_ingredient_dependency(
                    ingredient, int(i_quantity))
