from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
from src.models.ingredient import Restriction


# Req 1
def test_ingredient():
    # Testa a instância da classe Ingredient
    # e verifica os atributos name e restrictions
    ingredient = Ingredient("queijo mussarela")
    assert ingredient.name == "queijo mussarela"
    assert ingredient.restrictions == {
        Restriction.LACTOSE, Restriction.ANIMAL_DERIVED
    }

    # Testa a representação textual (__repr__) do ingrediente
    ingredient = Ingredient("queijo mussarela")
    assert repr(ingredient) == "Ingredient('queijo mussarela')"

    # Testa a igualdade (__eq__) entre dois ingredientes iguais e diferentes
    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("queijo mussarela")
    ingredient3 = Ingredient("bacon")
    assert ingredient1 == ingredient2
    assert ingredient1 != ingredient3

    # Testa o hash (__hash__) entre dois ingredientes iguais e diferentes
    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("queijo mussarela")
    ingredient3 = Ingredient("bacon")
    assert hash(ingredient1) == hash(ingredient2)
    assert hash(ingredient1) != hash(ingredient3)
