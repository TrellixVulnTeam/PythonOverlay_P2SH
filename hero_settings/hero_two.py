"""
    hero two depends on key values from GUI.HERO and hero settings
    It defines avatar, item and references file paths for hero two
"""
from GUI.hero import ITEM_DESC_KEY, ITEM_IMAGE_KEY, ITEM_DESC_NAME
from config import ITEMS_FILE_PATH, REFERENCES_FILE_PATH


# The path to the hero's avatar image
HERO_AVATAR_TWO = 'assets/images/heroes/anti_mage.png'

# The path to the hero's reference image
HERO_REFERENCE_TWO = 'assets/images/heroes/anti_mage_reference.png'


# The paths and description of each of the hero's items
ITEMS_TWO = [
    {
        ITEM_IMAGE_KEY: f"{ITEMS_FILE_PATH}band_of_elvenskin.png",
        ITEM_DESC_NAME: "Band of Elvenskin",
        ITEM_DESC_KEY: "Grants more of your primary attribute.\n(+6 Agility) (450 gold)"
    },
    {
        ITEM_IMAGE_KEY: f"{ITEMS_FILE_PATH}quelling_blade.png",
        ITEM_DESC_NAME: "Quelling Blade",
        ITEM_DESC_KEY: "Will help you last hit creeps easier.\n (130 gold)"
    },
    {
        ITEM_IMAGE_KEY: f"{ITEMS_FILE_PATH}slippers_of_agility.png",
        ITEM_DESC_NAME: "Slippers of agility",
        ITEM_DESC_KEY: "Grants more of your primary attribute.\n(+3 Agility) (145 gold)"
    },
    {
        ITEM_IMAGE_KEY: f"{ITEMS_FILE_PATH}blades_of_attack.png",
        ITEM_DESC_NAME: "Blades of Attack",
        ITEM_DESC_KEY: "Grants more attack damage.\n (+9 Attack "
                       "damage) (450 gold) "
    },
    {
        ITEM_IMAGE_KEY: f"{ITEMS_FILE_PATH}quarterstaff.png",
        ITEM_DESC_NAME: "Quarterstaff",
        ITEM_DESC_KEY: "Makes you attack faster and hit harder.\n(+10 Attack damage, +10 Attack speed) (875 "
                       "gold) "
    },
    {
        ITEM_IMAGE_KEY: f"{ITEMS_FILE_PATH}blade_of_alacrity.png",
        ITEM_DESC_NAME: "Blade of Alacrity",
        ITEM_DESC_KEY: "Grants more of your primary attribute.\n(+10 Agility) (1000 gold)"
    }
]


# The paths to each of the hero's item references
ITEMS_REFERENCES_TWO = [
    f"{REFERENCES_FILE_PATH}band_of_elvenskin.png",
    f"{REFERENCES_FILE_PATH}quelling_blade.png",
    f"{REFERENCES_FILE_PATH}slippers_of_agility.png",
    f"{REFERENCES_FILE_PATH}blades_of_attack.png",
    f"{REFERENCES_FILE_PATH}quarterstaff.png",
    f"{REFERENCES_FILE_PATH}blade_of_alacrity.png"
]


ITEMS_ACCEPTABLE_TWO = [
    10,
    10,
    10,
    10,
    12,
    13
]
