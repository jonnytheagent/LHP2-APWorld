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
        self.multiworld.push_precollected(self.create_item(ItemName.dt_unlock))

    def create_regions(self):
        self.seed_location_table = setup_locations(self.options)
        create_regions(self.multiworld, self.player, self.seed_location_table)

    def create_item(self, name: str) -> Item:
        data = item_data_table[name]
        item = LHP2Item(name, data.classification, data.code, self.player)
        return item

    def create_items(self):
        itempool = []
        for name, data in item_data_table.items():
            itempool += [self.create_item(name) for _ in range(data.qty)]
        self.multiworld.itempool.extend(itempool)

    def set_rules(self):
        set_rules(self.multiworld, self.options, self.player)
