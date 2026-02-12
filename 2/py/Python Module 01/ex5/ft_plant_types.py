#!/usr/bin/env python3
"""
Exercise 5: Specialized Plant Types

A program that demonstrates inheritance by creating a base Plant class
and specialized types (Flower, Tree, Vegetable) that inherit common features.
"""


class Plant:
    """
    Base class representing a plant with common features.

    Attributes:
        name (str): The name of the plant.
        height (int): The height of the plant in centimeters.
        age (int): The age of the plant in days.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize a Plant instance.

        Args:
            name: The name of the plant.
            height: The height in centimeters.
            age: The age in days.
        """
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        """
        Get basic plant information.

        Returns:
            A string representation of the plant.
        """
        return f"{self.name}: {self.height}cm, {self.age} days"


class Flower(Plant):
    """
    A specialized plant type representing a flower.

    Attributes:
        color (str): The color of the flower.
    """

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """
        Initialize a Flower instance.

        Args:
            name: The name of the flower.
            height: The height in centimeters.
            age: The age in days.
            color: The color of the flower.
        """
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """Display blooming information."""
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> str:
        """
        Get detailed flower information.

        Returns:
            A string representation of the flower with color.
        """
        return f"{self.name} (Flower): {self.height}cm, {self.age} days, " \
               f"{self.color} color"


class Tree(Plant):
    """
    A specialized plant type representing a tree.

    Attributes:
        trunk_diameter (float): The diameter of the trunk in centimeters.
    """

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        trunk_diameter: float
    ) -> None:
        """
        Initialize a Tree instance.

        Args:
            name: The name of the tree.
            height: The height in centimeters.
            age: The age in days.
            trunk_diameter: The diameter of the trunk in centimeters.
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> float:
        """
        Calculate the shade area produced by the tree.

        Returns:
            The approximate shade area in square meters.
        """
        shade_area = (self.trunk_diameter / 100) * self.height / 10
        return shade_area

    def get_info(self) -> str:
        """
        Get detailed tree information.

        Returns:
            A string representation of the tree with trunk diameter.
        """
        return f"{self.name} (Tree): {self.height}cm, {self.age} days, " \
               f"{self.trunk_diameter}cm diameter"


class Vegetable(Plant):
    """
    A specialized plant type representing a vegetable.

    Attributes:
        harvest_season (str): The season when the vegetable is harvested.
        nutritional_value (str): The nutritional benefits of the vegetable.
    """

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutritional_value: str
    ) -> None:
        """
        Initialize a Vegetable instance.

        Args:
            name: The name of the vegetable.
            height: The height in centimeters.
            age: The age in days.
            harvest_season: The season when it's harvested.
            nutritional_value: Its nutritional benefits.
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self) -> str:
        """
        Get detailed vegetable information.

        Returns:
            A string representation of the vegetable with season and nutrition.
        """
        return f"{self.name} (Vegetable): {self.height}cm, {self.age} days, " \
               f"{self.harvest_season} harvest"


if __name__ == "__main__":
    """Main program execution block."""
    print("=== Garden Plant Types ===")

    # Create Flower instances
    rose1 = Flower("Rose", 25, 30, "red")
    rose2 = Flower("Daisy", 40, 20, "white")

    # Create Tree instances
    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 600, 2000, 45)

    # Create Vegetable instances
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 30, 120, "fall", "beta-carotene")

    all_plants = [rose1, rose2, oak, pine, tomato, carrot]

    for plant in all_plants:
        print(plant.get_info())
        if isinstance(plant, Flower):
            plant.bloom()
        elif isinstance(plant, Tree):
            shade = plant.produce_shade()
            print(f"{plant.name} provides {shade:.0f} square meters of shade")
        elif isinstance(plant, Vegetable):
            print(f"{plant.name} is rich in {plant.nutritional_value}")
