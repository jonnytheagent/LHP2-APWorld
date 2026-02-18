from typing import Dict

from BaseClasses import Item, Tutorial
from Options import OptionError
from .Items import LHP2Item, item_data_table
from .Locations import all_location_table, LocationData, setup_locations
from .Names import ItemName, RegionName
from .Options import LHP2Options
from .Regions import create_regions, connect_regions
from .Rules import set_rules
from ..AutoWorld import World, WebWorld, CollectionState


class LHP2Web(WebWorld):
    theme = "ocean"
    tutorial = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Lego Harry Potter 5-7 Archipelago",
        "English",
        "setup_en.md",
        "setup/en",
        ["jrad"]
    )]


class LHP2World(World):
    """
    Save the Wizarding World from Lord Voldemort!
    """
    game = "Lego Harry Potter 5-7"
    options_dataclass = LHP2Options
    options: LHP2Options
    topology_present = True

    item_name_to_id = {name: data.code for name, data in item_data_table.items() if data.code is not None}
    location_name_to_id = {name: data.id for name, data in all_location_table.items()}

    seed_location_table: Dict[str, int]
    seed_item_table: Dict[str, int]

    data_version = 1
    web = LHP2Web()

    def generate_early(self):
        self.validate_yaml()
        self.multiworld.push_precollected(self.create_item(ItemName.dt_unlock))
        self.choose_starting_levels()

    def validate_yaml(self):
        if self.options.NumStartLevels > len(self.options.StartingLevelOptions.value) + 1:
            raise OptionError("You want to start with more levels than are in the starting pool")

    def create_regions(self):
        self.seed_location_table = setup_locations(self.options)
        create_regions(self.multiworld, self.player, self.seed_location_table)

    def create_item(self, name: str) -> Item:
        data = item_data_table[name]
        item = LHP2Item(name, data.classification, data.code, self.player)
        return item

    def create_items(self):
        itempool = []  # TODO: to break this out like Batman
        for name, data in item_data_table.items():
            itempool += [self.create_item(name) for _ in range(data.qty)]
        self.multiworld.itempool.extend(itempool)

    def set_rules(self):
        set_rules(self)

    def choose_starting_levels(self):
        levels_pushed: int = 1
        while levels_pushed < self.options.NumStartLevels.value:
            starting_level = self.random.choice(self.options.StartingLevelOptions.value)
            self.options.StartingLevelOptions.value.remove(starting_level)
            starting_level = starting_level + ": Level Unlocked"
            self.multiworld.push_precollected(self.create_item(starting_level))
            levels_pushed += 1

    def fill_slot_data(self):
        return {
            "EndGoal": self.options.EndGoal.value,
            "CollectiblesRequired": self.options.CollectibleQuantity.value,
            "FlawInThePlanCondition": self.options.FlawInThePlanCondition.value,
        }
