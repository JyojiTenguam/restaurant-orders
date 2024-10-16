import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str):
        self.dishes = set()
        self._load_menu_data(source_path)

    def _load_menu_data(self, source_path: str):
        """Lê o arquivo CSV e popula o set de pratos"""
        with open(source_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self._process_row(row)

    def _process_row(self, row: dict):
        """Processa uma linha do CSV e atualiza o set de pratos"""
        dish_name = row['dish']
        price = float(row['price'])
        ingredient_name = row['ingredient']
        recipe_amount = int(row['recipe_amount'])

        ingredient = Ingredient(ingredient_name)
        dish = self._get_or_create_dish(dish_name, price)
        dish.add_ingredient_dependency(ingredient, recipe_amount)

    def _get_or_create_dish(self, dish_name: str, price: float) -> Dish:
        """Recupera um prato existente ou cria um novo"""
        for dish in self.dishes:
            if dish.name == dish_name:
                return dish
        new_dish = Dish(dish_name, price)
        self.dishes.add(new_dish)
        return new_dish
