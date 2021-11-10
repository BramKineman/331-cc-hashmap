"""
Name:
Coding Challenge 7 - Lonely Rolling Star - Solution Code
CSE 331 Fall 2020
Professor Sebnem Onsay
"""
from typing import List, Tuple


class Item:
    """
    A class that will store an item's name and category
    """
    def __init__(self, item_name: str, item_category: str):
        self.name = item_name
        self.category = item_category

    def __repr__(self):
        return "Item('" + self.name + "','" + self.category + "')"

    def get_name(self) -> str:
        """
        returns the strng representing the item's name
        :return: Item name string
        """
        return self.name

    def get_category(self) -> str:
        """
        Returns the string representation of the item's category
        :return: Item category string
        """
        return self.category


class RoboKingOfAllCosmos:

    def __init__(self):
        self.score_book = {}

    def construct_score_book(self, items_and_size: List[Tuple[str, float]]) -> None:
        """
        Given a list of items and their associated size, adds them to the RoboKing's memory to be stored for later use.
        :param items_and_size: List of items and their sizes as Tuples.
        :return: None.
        """
        self.score_book = {}

        for item, size in items_and_size:
            self.score_book[item] = size

    def get_score_book(self) -> List[Tuple[str, float]]:
        """
        Finds and returns the contents of the current scoring container.
        :return: Current scoring container as a Tuple[str, float]
        """
        returned = []

        for item, size in self.score_book.items():
            my_tuple = item, size
            returned.append(my_tuple)

        return returned

    def judge_katamari(self, katamari_contents: List[Item]) -> Tuple[float, List[Tuple[str, int]], List[str]]:
        """
        Determines the size of a katamari, its top three categories, and its cousins.
        :param katamari_contents: Contents of the katamari to determine on.
        :return: Tuple containing the katamari's size, a list containing the top three categories of items and how
        many were in each categories, and a list of any found cousins.
        """
        size_total = 0
        cousins = []
        my_dict = {}

        for items in katamari_contents:
            # keep track of cousins
            if items.category == "cousins":
                cousins.append(items.name)
            # cousins do not contribute to size.
            if items.category != "cousins":
                size_total += self.score_book[items.name]

            # if in my dictionary, increment frequency value
            if my_dict.get(items.category) is not None:
                my_dict[items.category] += 1
            else:
                # if not in the dictionary, add it with frequency value of 1
                my_dict[items.category] = 1

        list_of_tuples = list(my_dict.items())
        # (x[1], x[0]) causes sort to check key value if values are equivalent.
        list_of_tuples.sort(key=lambda x: (x[1], x[0]), reverse=True)
        top_categories = list_of_tuples[:3]

        return round(size_total, 1), top_categories, cousins
