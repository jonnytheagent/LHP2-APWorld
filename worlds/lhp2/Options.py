from dataclasses import dataclass
from typing import List
from Options import DefaultOnToggle, Toggle, Range, Choice, PerGameCommonOptions, OptionList, OptionDict
from .Names import ItemName


class EndGoal(Choice):
    """
    Determine the goal for the seed

    Defeat Voldemort: Collect the 6 Horcruxes and defeat Voldemort in The Flaw in the Plan
    The Collector: Collect items from throughout the multiworld to win
    """
    display_name = "Goal"
    option_defeat_voldemort = 0
    option_the_collector = 1
    default = 0


class CollectibleQuantity(OptionDict):
    """
    The number of each collectible you need to beat the seed. Does nothing if the collector is your not win con.

    Valid Keys:
    - Character Token
    - Gold Brick
    - House Crest Completed
    - Student in Peril
    - True Wizard
    """
    display_name = "Collectibles Required"
    min = 0
    max_values_dict: dict[str, int] = {
        ItemName.gb: 200,
        ItemName.sip: 60,
        ItemName.tw: 24,
        ItemName.ct: 200,
        ItemName.hcgb: 24,
    }
    default = {ItemName.gb: 100, ItemName.sip: 30, ItemName.tw: 12, ItemName.ct: 100, ItemName.hcgb: 12}


class FlawInThePlanCondition(Choice):
    """
    Determine the Level Unlock Condition for The Flaw in The Plan. Does nothing if Voldemort is not the goal.
    """
    display_name = "Flaw In The Plan Unlock Condition"
    option_horcruxes = 0
    option_level_shuffled = 1
    default = 0

class NumStartLevels(Range):
    """
    Determine the number of starting levels.
    """
    display_name = "Number of Starting Levels"
    range_start = 1
    range_end = 24
    default = 1


class StartingLevelOptions(OptionList):
    """
    Determines which levels you start with.
    Please note due to technical limitations, you will always start with Dark Times.

    Valid Keys:
    "Dumbledore's Army"
    "Focus!"
    "Kreacher Discomforts"
    "A Giant Virtuoso"
    "A Veiled Threat"
    "Out of Retirement"
    "Just Desserts"
    "A Not So Merry Christmas"
    "Love Hurts"
    "Felix Felicis"
    "The Horcrux and the Hand"
    "The Seven Harry's"
    "Magic is Might"
    "In Grave Danger"
    "Sword and Locket"
    "Lovegood's Lunacy"
    "DOBBY!"
    "The Thief's Downfall"
    "Back to School"
    "Burning Bridges"
    "Fiendfyre Frenzy"
    "Snape's Tears"
    "The Flaw in the Plan"
    """

    display_name = "Starting Level Options"

    valid_keys = {
        "Dumbledore's Army",
        "Focus!",
        "Kreacher Discomforts",
        "A Giant Virtuoso",
        "A Veiled Threat",
        "Out of Retirement",
        "Just Desserts",
        "A Not So Merry Christmas",
        "Love Hurts",
        "Felix Felicis",
        "The Horcrux and the Hand",
        "The Seven Harrys",
        "Magic is Might",
        "In Grave Danger",
        "Sword and Locket",
        "Lovegood's Lunacy",
        "DOBBY!",
        "The Thief's Downfall",
        "Back to School",
        "Burning Bridges",
        "Fiendfyre Frenzy",
        "Snape's Tears",
        "The Flaw in the Plan",
    }

    default = [
        "Dumbledore's Army",
        "Focus!",
        "Kreacher Discomforts",
        "A Giant Virtuoso",
        "A Veiled Threat",
        "Out of Retirement",
        "Just Desserts",
        "A Not So Merry Christmas",
        "Love Hurts",
        "Felix Felicis",
        "The Horcrux and the Hand",
        "The Seven Harrys",
        "Magic is Might",
        "In Grave Danger",
        "Sword and Locket",
        "Lovegood's Lunacy",
        "DOBBY!",
        "The Thief's Downfall",
        "Back to School",
        "Burning Bridges",
        "Fiendfyre Frenzy",
        "Snape's Tears",
        "The Flaw in the Plan",
    ]


class HardPurchases(Toggle):
    """
    Turning this on makes it so purchases no longer require a stud multiplier.
    """
    display_name = "Hard Purchases"


class LowMultiplierPriceMinimum(Range):
    """
    Determines the starting price for a low multiplier.
    A low multiplier is defined as any multiplier.
    """
    display_name = "Low Multiplier Price Minimum"
    range_start = 10
    range_end = 10000000
    default = 50000


class HighMultiplierMinimum(Range):
    """
    Determines the starting price for a high multiplier.
    Must be larger than Low Multiplier Price.
    A high multiplier is defined as Score x6, Score x8, Score x10 or both Score x2 and Score x4.
    """
    display_name = "High Multiplier Price Minimum"
    range_start = 10
    range_end = 10000000
    default = 100000


@dataclass
class LHP2Options(PerGameCommonOptions):
    EndGoal: EndGoal
    CollectibleQuantity: CollectibleQuantity
    FlawInThePlanCondition: FlawInThePlanCondition
    NumStartLevels: NumStartLevels
    StartingLevelOptions: StartingLevelOptions
    HardPurchases: HardPurchases
    LowMultiplierPriceMinimum: LowMultiplierPriceMinimum
    HighMultiplierMinimum: HighMultiplierMinimum
