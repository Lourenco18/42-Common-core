#!/usr/bin/env python3
"""
Exercise 6: Garden Analytics Platform

A comprehensive garden data analytics platform that processes and analyzes
garden data using nested components and inheritance chains.
"""


class Plant:
    """Base class representing a plant."""

    def __init__(self, name: str, height: int = 0) -> None:
        """
        Initialize a Plant instance.

        Args:
            name: The name of the plant.
            height: The initial height in centimeters.
        """
        self.name = name
        self.height = height

    def grow(self) -> None:
        """Make the plant grow by 1 centimeter."""
        self.height += 1

    def get_info(self) -> str:
        """
        Get basic plant information.

        Returns:
            A string representation of the plant.
        """
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """A plant that produces flowers."""

    def __init__(
        self,
        name: str,
        height: int = 0,
        color: str = "unknown"
    ) -> None:
        """
        Initialize a FloweringPlant instance.

        Args:
            name: The name of the plant.
            height: The initial height in centimeters.
            color: The color of the flowers.
        """
        super().__init__(name, height)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        """Make the plant bloom."""
        self.is_blooming = True

    def get_info(self) -> str:
        """
        Get flowering plant information.

        Returns:
            A string representation of the flowering plant.
        """
        bloom_status = "blooming" if self.is_blooming else "not blooming"
        return f"{self.name}: {self.height}cm, {self.color} flowers ({bloom_status})"


class PrizeFlower(FloweringPlant):
    """A flowering plant with prize points."""

    def __init__(
        self,
        name: str,
        height: int = 0,
        color: str = "unknown",
        prize_points: int = 0
    ) -> None:
        """
        Initialize a PrizeFlower instance.

        Args:
            name: The name of the plant.
            height: The initial height in centimeters.
            color: The color of the flowers.
            prize_points: Competition prize points.
        """
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def get_info(self) -> str:
        """
        Get prize flower information.

        Returns:
            A string representation of the prize flower.
        """
        bloom_status = "blooming" if self.is_blooming else "not blooming"
        return f"{self.name}: {self.height}cm, {self.color} flowers ({bloom_status}), Prize points: {self.prize_points}"


class GardenStats:
    """Helper class for calculating garden statistics."""

    def __init__(self) -> None:
        """Initialize a GardenStats instance."""
        self.plants_added = 0
        self.total_growth = 0
        self.plant_types_count = {"regular": 0, "flowering": 0, "prize": 0}

    def record_growth(self, amount: int) -> None:
        """
        Record plant growth.

        Args:
            amount: The amount of growth in centimeters.
        """
        self.total_growth += amount

    def record_plant(self, plant: Plant) -> None:
        """
        Record a plant addition.

        Args:
            plant: The plant being added.
        """
        self.plants_added += 1
        if isinstance(plant, PrizeFlower):
            self.plant_types_count["prize"] += 1
        elif isinstance(plant, FloweringPlant):
            self.plant_types_count["flowering"] += 1
        else:
            self.plant_types_count["regular"] += 1

    def validate_height(self, height: int) -> bool:
        """
        Validate a plant height.

        Args:
            height: The height to validate.

        Returns:
            True if the height is valid (non-negative), False otherwise.
        """
        return height >= 0


class Garden:
    """A garden that manages multiple plants."""

    def __init__(self, owner: str) -> None:
        """
        Initialize a Garden instance.

        Args:
            owner: The name of the garden owner.
        """
        self.owner = owner
        self.plants: list[Plant] = []
        self.stats = GardenStats()

    def add_plant(self, plant: Plant) -> None:
        """
        Add a plant to the garden.

        Args:
            plant: The plant to add.
        """
        self.plants.append(plant)
        self.stats.record_plant(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_plants_grow(self) -> None:
        """Help all plants in the garden grow."""
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            initial_height = plant.height
            plant.grow()
            growth = plant.height - initial_height
            self.stats.record_growth(growth)
            print(f"{plant.name} grew {growth}cm")

    def get_report(self) -> str:
        """
        Get a report of the garden's status.

        Returns:
            A formatted report string.
        """
        report = f"=== {self.owner}'s Garden Report ===\n"
        report += "Plants in garden:\n"
        for plant in self.plants:
            report += f"- {plant.get_info()}\n"
        report += f"Plants added: {self.stats.plants_added}, Total growth: {self.stats.total_growth}cm\n"
        report += f"Plant types: {self.stats.plant_types_count['regular']} regular, {self.stats.plant_types_count['flowering']} flowering, {self.stats.plant_types_count['prize']} prize flowers"
        return report


class GardenManager:
    """Manager for multiple gardens."""

    gardens: dict[str, Garden] = {}

    def __init__(self) -> None:
        """Initialize a GardenManager instance."""
        pass

    @classmethod
    def create_garden(cls, owner: str) -> Garden:
        """
        Create a new garden for an owner.

        Args:
            owner: The name of the garden owner.

        Returns:
            A new Garden instance.
        """
        if owner not in cls.gardens:
            cls.gardens[owner] = Garden(owner)
        return cls.gardens[owner]

    @staticmethod
    def validate_height(height: int) -> bool:
        """
        Validate a plant height (utility function).

        Args:
            height: The height to validate.

        Returns:
            True if the height is valid (non-negative), False otherwise.
        """
        return height >= 0

    @classmethod
    def create_garden_network(cls) -> str:
        """
        Create a garden network (class method working on manager type itself).

        Returns:
            A string describing the network.
        """
        return f"Garden Network: {len(cls.gardens)} gardens managed"

    @classmethod
    def get_garden_scores(cls) -> dict[str, int]:
        """
        Calculate scores for all gardens.

        Returns:
            A dictionary mapping garden owner names to their scores.
        """
        scores = {}
        for owner, garden in cls.gardens.items():
            score = sum(plant.height for plant in garden.plants)
            scores[owner] = score
        return scores


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")

    alice_garden = GardenManager.create_garden("Alice")
    bob_garden = GardenManager.create_garden("Bob")

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    rose.bloom()
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)
    sunflower.bloom()

    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    alice_garden.help_plants_grow()

    print()
    print(alice_garden.get_report())

    bob_garden.add_plant(Plant("Cactus", 20))
    bob_garden.add_plant(Plant("Fern", 45))

    print()
    print(GardenManager.validate_height(100))
    print()
    print(GardenManager.create_garden_network())

    scores = GardenManager.get_garden_scores()
    print("Garden scores - " +
          ", ".join(f"{owner}: {score}" for owner, score in scores.items()))
    print(f"Total gardens managed: {len(GardenManager.gardens)}")
