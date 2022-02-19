from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)

from typing import List, Set, Tuple

# flake8: noqa: E501


def clean_ingredients(dish_name: str, dish_ingredients: List[str]) -> Tuple[str, Set]:
    """

    :param dish_name: str
    :param dish_ingredients: list
    :return: tuple of (dish_name, ingredient set)

    This function should return a `tuple` with the name of the dish as the first item,
    followed by the de-duped `set` of ingredients as the second item.

    ```python
    >>> clean_ingredients('Punjabi-Style Chole', ['onions', 'tomatoes', 'ginger paste', 'garlic paste', 'ginger paste', 'vegetable oil', 'bay leaves', 'cloves', 'cardamom', 'cilantro', 'peppercorns', 'cumin powder', 'chickpeas', 'coriander powder', 'red chili powder', 'ground turmeric', 'garam masala', 'chickpeas', 'ginger', 'cilantro'])

    >>> ('Punjabi-Style Chole', {'garam masala', 'bay leaves', 'ground turmeric', 'ginger', 'garlic paste', 'peppercorns', 'ginger paste', 'red chili powder', 'cardamom', 'chickpeas', 'cumin powder', 'vegetable oil', 'tomatoes', 'coriander powder', 'onions', 'cilantro', 'cloves'})
```
    """
    return (dish_name, set(dish_ingredients))


def check_drinks(drink_name: str, drink_ingredients: List[str]) -> str:
    """

    :param drink_name: str
    :param drink_ingredients: list
    :return: str drink name + ("Mocktail" or "Cocktail")

    The function should return the name of the drink followed by "Mocktail" if the drink has
    no alcoholic ingredients, and drink name followed by "Cocktail" if the drink includes alcohol.

    ```python
    >>> from sets_categories_data import ALCOHOLS
    >>> check_drinks('Honeydew Cucumber', ['honeydew', 'coconut water', 'mint leaves', 'lime juice', 'salt', 'english cucumber'])
    'Honeydew Cucumber Mocktail'

    >>> check_drinks('Shirley Tonic', ['cinnamon stick', 'scotch', 'whole cloves', 'ginger', 'pomegranate juice', 'sugar', 'club soda'])
    'Shirley Tonic Cocktail'
    ```
    """

    alcoholic = any([ingr in ALCOHOLS for ingr in drink_ingredients])
    return drink_name + ' Cocktail' if alcoholic else drink_name + ' Mocktail'


def categorize_dish(dish_name: str, dish_ingredients: List[str]) -> str:
    """

    :param dish_name: str
    :param dish_ingredients: list
    :return: str "dish name: CATEGORY"

    This function should return a string with the `dish name: <CATEGORY>` (which meal category the dish belongs to).
    All dishes will "fit" into one of the categories imported from `sets_categories_data.py`
    (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).

    ```python
    >>> from sets_categories_data import VEGAN, VEGETARIAN, PALEO, KETO, OMNIVORE

    >>> categorize_dish('Sticky Lemon Tofu', ['tofu', 'soy sauce', 'salt', 'black pepper', 'cornstarch', 'vegetable oil', 'garlic', 'ginger', 'water', 'vegetable stock', 'lemon juice', 'lemon zest', 'sugar'])

    'Sticky Lemon Tofu: VEGAN'
    ```
    """

    # from less to more restrictive or is it a vote?
    # No: just check inclusion all ingredients in given Category => dish is of that category
    cats = {  # mapping
        'OMNIVORE': OMNIVORE,
        'KETO': KETO,
        'PALEO': PALEO,
        'VEGETARIAN': VEGETARIAN,
        'VEGAN':  VEGAN
    }
    for cat_str, cat_set in cats.items():
        if all([ingr in cat_set for ingr in dish_ingredients]):
            return dish_name + f': {cat_str}'


def tag_special_ingredients(dish: Tuple[str, List[str]]) -> Tuple[str, Set[str]]:
    """

    :param dish: tuple of (str of dish name, list of dish ingredients)
    :return: tuple of (str of dish name, set of dish special ingredients)

    Return the dish name followed by the `set` of ingredients that require a special note on the dish description.
    For the purposes of this exercise, all allergens or special ingredients that need to be tracked are in the
    SPECIAL_INGREDIENTS constant imported from `sets_categories_data.py`.

    ```python
    >>> from sets_categories_data import SPECIAL_INGREDIENTS

    >>> tag_special_ingredients(('Ginger Glazed Tofu Cutlets', ['tofu', 'soy sauce', 'ginger', 'corn starch', 'garlic', 'brown sugar', 'sesame seeds', 'lemon juice']))
    ...
    ('Ginger Glazed Tofu Cutlets', {'garlic','soy sauce','tofu'})
    """

    tag_set = {
        ingr for ingr in dish[1] if ingr in SPECIAL_INGREDIENTS
    }
    return (dish[0], tag_set)


def compile_ingredients(dishes: List[Set[str]]) -> Set[str]:
    """

    :param dishes: list of dish ingredient sets
    :return: set

    This function should return a `set` of all ingredients from all listed dishes.

    ```python
    dishes = [ {'tofu', 'soy sauce', 'ginger', 'corn starch', 'garlic', 'brown sugar', 'sesame seeds', 'lemon juice'},
           {'pork tenderloin', 'arugula', 'pears', 'blue cheese', 'pine nuts',
           'balsamic vinegar', 'onions', 'black pepper'},
           {'honeydew', 'coconut water', 'mint leaves', 'lime juice', 'salt', 'english cucumber'}]

    >>> compile_ingredients(dishes)
    ...
    {'arugula', 'brown sugar', 'honeydew', 'coconut water', 'english cucumber', 'balsamic vinegar', 'mint leaves', 'pears', 'pork tenderloin', 'ginger', 'blue cheese', 'soy sauce', 'sesame seeds', 'black pepper', 'garlic', 'lime juice', 'corn starch', 'pine nuts', 'lemon juice', 'onions', 'salt', 'tofu'}
    ```
    """

    comp_set = {*dishes[0]}
    for ix in range(1, len(dishes)):
        comp_set = comp_set.union(dishes[ix])
    return comp_set


def separate_appetizers(dishes: List[str], appetizers: List[str]) -> List[str]:
    """

    :param dishes: list of dish names
    :param appetizers: list of appetizer names
    :return: list of dish names

    The function should return the list of dish names with appetizer names removed.
    Either list could contain duplicates and may require de-duping.

    ```python
    dishes =    ['Avocado Deviled Eggs','Flank Steak with Chimichurri and Asparagus', 'Kingfish Lettuce Cups',
             'Grilled Flank Steak with Caesar Salad','Vegetarian Khoresh Bademjan','Avocado Deviled Eggs',
             'Barley Risotto','Kingfish Lettuce Cups']

    appetizers = ['Kingfish Lettuce Cups','Avocado Deviled Eggs','Satay Steak Skewers',
              'Dahi Puri with Black Chickpeas','Avocado Deviled Eggs','Asparagus Puffs',
              'Asparagus Puffs']

    >>> separate_appetizers(dishes, appetizers)
    ...
    ['Vegetarian Khoresh Bademjan', 'Barley Risotto', 'Flank Steak with Chimichurri and Asparagus',
    'Grilled Flank Steak with Caesar Salad']
    ```
    """

    return [
        dish for dish in set(dishes) if dish not in appetizers
    ]


def singleton_ingredients(dishes: List[str], interset) -> Set[str]:
    """

    :param intersection: constant - one of (VEGAN_INTERSECTION,VEGETARIAN_INTERSECTION,PALEO_INTERSECTION,
                                            KETO_INTERSECTION,OMNIVORE_INTERSECTION)
    :param dishes:  list of ingredient sets
    :return: set of singleton ingredients

    Each dish is represented by a `set` of its ingredients.
    Each `<CATEGORY>_INTERSECTION` is an `intersection` of all dishes in the category.
    The function should return a `set` of ingredients that only appear in a single dish.

    ```python
    from sets_categories_data import example_dishes, EXAMPLE_INTERSECTION

    >>> singleton_ingredients(example_dishes, EXAMPLE_INTERSECTION)
    ...
    {'vegetable oil', 'vegetable stock', 'barley malt', 'tofu', 'fresh basil', 'lemon', 'ginger', 'honey', 'spaghetti', 'cornstarch', 'yeast', 'red onion', 'breadcrumbs', 'mixed herbs', 'garlic powder', 'celeriac', 'lemon zest', 'sunflower oil', 'mushrooms', 'silken tofu', 'smoked tofu', 'bell pepper', 'cashews', 'oregano', 'tomatoes', 'parsley', 'red pepper flakes', 'rosemary'}
    ```
    """
    all_set = set()
    for dish in dishes:
        # we want complement of intersection, also |: union, &: intersection
        all_set |= dish - (interset & dish)
    return all_set
