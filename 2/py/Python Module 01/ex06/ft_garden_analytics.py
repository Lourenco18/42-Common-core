

class Plant:
   

    def __init__(self, name: str, height: int = 0) -> None:
   
        self.name = name
        self.height = height

    def grow(self) -> None:
   
        self.height += 1

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
   

    def __init__(
        self,
        name: str,
        height: int = 0,
        color: str = "unknown"
    ) -> None:
        super().__init__(name, height)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
      
        self.is_blooming = True

    def get_info(self) -> str:
        bloom_status = "blooming" if self.is_blooming else "not blooming"
        return f"{self.name}: {self.height}cm, {self.color} flowers " \
               f"({bloom_status})"


class PrizeFlower(FloweringPlant):
   

    def __init__(
        self,
        name: str,
        height: int = 0,
        color: str = "unknown",
        prize_points: int = 0
    ) -> None:
   
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def get_info(self) -> str:
        bloom_status = "blooming" if self.is_blooming else "not blooming"
        return f"{self.name}: {self.height}cm, {self.color} flowers " \
               f"({bloom_status}), Prize points: {self.prize_points}"


class GardenStats:
   

    def __init__(self) -> None:
   
        self.plants_added = 0
        self.total_growth = 0
        self.plant_types_count = {"regular": 0, "flowering": 0, "prize": 0}

    def record_growth(self, amount: int) -> None:
        self.total_growth += amount

    def record_plant(self, plant: Plant) -> None:
        self.plants_added += 1
        if isinstance(plant, PrizeFlower):
            self.plant_types_count["prize"] += 1
        elif isinstance(plant, FloweringPlant):
            self.plant_types_count["flowering"] += 1
        else:
            self.plant_types_count["regular"] += 1

    def validate_height(self, height: int) -> bool:
        return height >= 0


class Garden:
    

    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants: list[Plant] = []
        self.stats = GardenStats()

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        self.stats.record_plant(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_plants_grow(self) -> None:
    
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            initial_height = plant.height
            plant.grow()
            growth = plant.height - initial_height
            self.stats.record_growth(growth)
            print(f"{plant.name} grew {growth}cm")

    def get_report(self) -> str:
        report = f"=== {self.owner}'s Garden Report ===\n"
        report += "Plants in garden:\n"
        for plant in self.plants:
            report += f"- {plant.get_info()}\n"
        report += f"Plants added: {self.stats.plants_added}, " \
                  f"Total growth: {self.stats.total_growth}cm\n"
        report += f"Plant types: {self.stats.plant_types_count['regular']} " \
                  f"regular, {self.stats.plant_types_count['flowering']} " \
                  f"flowering, {self.stats.plant_types_count['prize']} " \
                  f"prize flowers"
        return report


class GardenManager:
    

    gardens: dict[str, Garden] = {}

    def __init__(self) -> None:
    
        pass

    @classmethod
    def create_garden(cls, owner: str) -> Garden:
        if owner not in cls.gardens:
            cls.gardens[owner] = Garden(owner)
        return cls.gardens[owner]

    @staticmethod
    def validate_height(height: int) -> bool:
        return height >= 0

    @classmethod
    def create_garden_network(cls) -> str:
        
        return f"Garden Network: {len(cls.gardens)} gardens managed"

    @classmethod
    def get_garden_scores(cls) -> dict[str, int]:
        
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

    # Simulate growth
    alice_garden.help_plants_grow()

    print()
    print(alice_garden.get_report())

    # Add some plants to Bob's garden
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
