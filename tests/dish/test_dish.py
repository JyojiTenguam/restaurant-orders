import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction


def test_dish():
    # Testa se a classe pode ser instanciada corretamente
    dish = Dish("Pasta", 12.99)
    assert dish.name == "Pasta"
    assert dish.price == 12.99

    # Testa se um TypeError é levantado para um preço de tipo inválido
    with pytest.raises(TypeError):
        Dish("Pasta", "doze e noventa e nove")

    # Testa se um ValueError é levantado para um preço inválido
    with pytest.raises(ValueError):
        Dish("Pasta", -10)

    # Testa se o método __repr__ funciona como esperado
    dish = Dish("Pasta", 12.99)
    assert repr(dish) == "Dish('Pasta', R$12.99)"

    # Testa se o método __eq__ funciona como esperado
    dish1 = Dish("Pasta", 12.99)
    dish2 = Dish("Pasta", 12.99)
    dish3 = Dish("Pizza", 15.99)
    assert dish1 == dish2
    assert dish1 != dish3

    # Testa se o método __hash__ funciona como esperado
    assert hash(dish1) == hash(dish2)
    assert hash(dish1) != hash(dish3)

    # Testa se o dicionário de receita do prato devolve
    # a quantidade correta de um ingrediente
    dish = Dish("Pasta", 12.99)
    ingredient = Ingredient("farinha")
    dish.add_ingredient_dependency(ingredient, 300)
    assert dish.recipe.get(ingredient) == 300

    # Testa se o método get_restrictions retorna
    # o conjunto correto de restrições
    dish = Dish("Pasta", 12.99)
    ingredient1 = Ingredient("farinha")
    ingredient2 = Ingredient("queijo mussarela")
    dish.add_ingredient_dependency(ingredient1, 300)
    dish.add_ingredient_dependency(ingredient2, 150)
    expected_restrictions = {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
        Restriction.GLUTEN
    }
    assert dish.get_restrictions() == expected_restrictions

    # Testa se o método get_ingredients retorna
    # o conjunto correto de ingredientes
    dish = Dish("Pasta", 12.99)
    ingredient1 = Ingredient("farinha")
    ingredient2 = Ingredient("queijo mussarela")
    dish.add_ingredient_dependency(ingredient1, 300)
    dish.add_ingredient_dependency(ingredient2, 150)
    expected_ingredients = {ingredient1, ingredient2}
    assert dish.get_ingredients() == expected_ingredients
