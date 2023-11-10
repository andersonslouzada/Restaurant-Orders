import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


def test_dish():
    churrasco = Dish("Churrasco", 30.50)
    assert churrasco.name == "Churrasco"
    assert churrasco.__hash__() == hash(churrasco.__repr__())
    assert churrasco.__repr__() == "Dish('Churrasco', R$30.50)"

    churrasco2 = Dish("Churrasco", 30.50)
    assert churrasco.__eq__(churrasco2) is True

    frutos_do_mar = Dish("Frutos do Mar", 50.00)
    assert frutos_do_mar.__eq__(churrasco) is False

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("error", "error")

    with pytest.raises(ValueError,
                       match="Dish price must be greater then zero."):
        Dish("error", 0.00)

    carne = Ingredient("carne")
    churrasco.add_ingredient_dependency(carne, 100)
    assert carne in churrasco.get_ingredients()
    assert Restriction.ANIMAL_DERIVED in churrasco.get_restrictions()
    assert Restriction.ANIMAL_MEAT in churrasco.get_restrictions()
