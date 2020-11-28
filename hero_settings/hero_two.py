"""
    hero two depends on key values from GUI.HERO and hero settings
    It defines avatar, item and references file paths for hero two
"""
from GUI.hero import ITEM_DESC_KEY, ITEM_IMAGE_KEY, ITEM_DESC_NAME
from config import ITEMS_FILE_PATH, REFERENCES_FILE_PATH


# The path to the hero's avatar image
HERO_AVATAR_TWO = 'assets/images/heroes/anti_mage.png'


# The paths and description of each of the hero's items
ITEMS_TWO = [
    {
        ITEM_IMAGE_KEY: f"{ITEMS_FILE_PATH}quelling_blade.png",
        ITEM_DESC_NAME: "Quelling Blade",
        ITEM_DESC_KEY: "The axe of a fallen gnome, it allows you to effectively\nmaneuver the forest. (130 gold)"
    },
    {
        ITEM_IMAGE_KEY: f"{ITEMS_FILE_PATH}belt_of_strength.png",
        ITEM_DESC_NAME: "Belt of Strength",
        ITEM_DESC_KEY: "A valued accessory for improving vitality. (+6 Strength)\n(450 gold)"
    },
    {
        ITEM_IMAGE_KEY: f"{ITEMS_FILE_PATH}crown.png",
        ITEM_DESC_NAME: "Crown",
        ITEM_DESC_KEY: "No description. (+4 Strength, +4 Agility, +4 Intelligence)\n(450 gold)"
    },
    {
        ITEM_IMAGE_KEY: f"{ITEMS_FILE_PATH}boots_of_speed.png",
        ITEM_DESC_NAME: "Boots of Speed",
        ITEM_DESC_KEY: "Fleet footwear, increasing movement.\n(+45 Movement speed) (500 gold)"
    },
    {
        ITEM_IMAGE_KEY: f"{ITEMS_FILE_PATH}chainmail.png",
        ITEM_DESC_NAME: "Chainmail",
        ITEM_DESC_KEY: "A medium weave of metal chains. (+4 Armor)\n(550 gold)"
    },
    {
        ITEM_IMAGE_KEY: f"{ITEMS_FILE_PATH}ogre_axe.png",
        ITEM_DESC_NAME: "Ogre Axe",
        ITEM_DESC_KEY: "You grow stronger just by holding it. (+10 Strength)\n(1000 gold)"
    }
]


# The paths to each of the hero's item references
ITEMS_REFERENCES_TWO = [
    f"{REFERENCES_FILE_PATH}aaaa5.png",
    f"{REFERENCES_FILE_PATH}aaaa.png",
    f"{REFERENCES_FILE_PATH}aaaa2.png",
    f"{REFERENCES_FILE_PATH}aaaa6.png",
    f"{REFERENCES_FILE_PATH}aaaa3.png",
    f"{REFERENCES_FILE_PATH}aaaa7.png"
]
