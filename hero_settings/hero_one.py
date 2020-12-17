"""
    hero one depends on key values from GUI.HERO and config
    It defines avatar, item and references file paths for hero one
"""
from GUI.hero import ITEM_DESC_KEY, ITEM_IMAGE_KEY, ITEM_DESC_NAME
from config import ITEMS_FILE_PATH, REFERENCES_FILE_PATH


# The path to the hero's avatar image
HERO_AVATAR_ONE = 'assets/images/heroes/underlord.png'

# The path to the hero's reference image
HERO_REFERENCE_ONE = 'assets/images/heroes/underlord_reference.png'


# The paths and description of each of the hero's items
ITEMS_ONE = [
    {
        ITEM_IMAGE_KEY: f"{ITEMS_FILE_PATH}quelling_blade.png",
        ITEM_DESC_NAME: "Quelling Blade",
        ITEM_DESC_KEY: "Will help you last hit creeps easier. (130 gold)"
    },
    {
        ITEM_IMAGE_KEY: f"{ITEMS_FILE_PATH}belt_of_strength.png",
        ITEM_DESC_NAME: "Belt of Strength",
        ITEM_DESC_KEY: "Grants more of your primary attribute. (+6 Strength)\n(450 gold)"
    },
    {
        ITEM_IMAGE_KEY: f"{ITEMS_FILE_PATH}crown.png",
        ITEM_DESC_NAME: "Crown",
        ITEM_DESC_KEY: "Gives you a little bit of damage, health and mana. \n(+4 Strength, +4 Agility, +4 Intelligence) (450 gold)"
    },
    {
        ITEM_IMAGE_KEY: f"{ITEMS_FILE_PATH}boots_of_speed.png",
        ITEM_DESC_NAME: "Boots of Speed",
        ITEM_DESC_KEY: "Makes you move around faster. \n(+45 Movement speed) (500 gold)"
    },

    {
        ITEM_IMAGE_KEY: f"{ITEMS_FILE_PATH}chainmail.png",
        ITEM_DESC_NAME: "Chainmail",
        ITEM_DESC_KEY: "Makes you take less damage from physical attacks. (+4 Armor)\n(550 gold)"
    },
    {
        ITEM_IMAGE_KEY: f"{ITEMS_FILE_PATH}ogre_axe.png",
        ITEM_DESC_NAME: "Ogre Axe",
        ITEM_DESC_KEY: "Grants more of your primary attribute. (+10 Strength)\n(1000 gold)"
    }
]


# The paths to each of the hero's item references
ITEMS_REFERENCES_ONE = [
    f"{REFERENCES_FILE_PATH}quelling_blade.png",
    f"{REFERENCES_FILE_PATH}belt_of_strength.png",
    f"{REFERENCES_FILE_PATH}crown.png",
    f"{REFERENCES_FILE_PATH}boots_of_speed.png",
    f"{REFERENCES_FILE_PATH}chainmail.png",
    f"{REFERENCES_FILE_PATH}ogre_axe.png"
]


ITEMS_ACCEPTABLE_ONE = [
    10,
    10,
    10,
    10,
    10,
    10
]
