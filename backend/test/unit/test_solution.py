import pytest
from unittest import mock
from unittest.mock import patch
from src.controllers.recipecontroller import RecipeController
# add your test case implementation here



@pytest.mark.unit
def test():
    pass

@pytest.mark.unit
@patch('src.controllers.recipecontroller', return_value={"Banana Bread": 0.5})
def test_normal_optimized(get_readiness_of_recipes):
    mocked_diet = mock.MagicMock()
    mocked_diet.name = 'NORMAL'
    mocked_dao = mock.MagicMock()
    rc = RecipeController(mocked_dao)
    assert rc.get_recipe(mocked_diet, True) == "Banana Bread"