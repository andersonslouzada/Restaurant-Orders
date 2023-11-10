from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


def test_ingredient():
    ingredient = Ingredient("queijo mussarela")
    assert ingredient.name == "queijo mussarela"

    restrictions = {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED}
    assert ingredient.restrictions == restrictions

    assert ingredient.__repr__() == "Ingredient('queijo mussarela')"

    ingredient2 = Ingredient("queijo mussarela")
    assert ingredient.__eq__(ingredient2) is True

    assert ingredient.__hash__() == hash(ingredient.name)
