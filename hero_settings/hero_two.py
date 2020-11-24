"""
    hero two depends on key values from GUI.HERO and hero settings
    It defines avatar, item and references file paths for hero two
"""
from GUI.hero import ITEM_DESC_KEY, ITEM_IMAGE_KEY
from config import ITEMS_FILE_PATH, REFERENCES_FILE_PATH


# The path to the hero's avatar image
HERO_AVATAR_TWO = 'assets/images/heroes/anti_mage.png'


# The paths and description of each of the hero's items
ITEMS_TWO = [
    {
        ITEM_IMAGE_KEY: f"{ITEMS_FILE_PATH}chainmail.png",
        ITEM_DESC_KEY: "Lorem ipsum dolor sit\namet, consectetur."
    },
    {
        ITEM_IMAGE_KEY: f"{ITEMS_FILE_PATH}crown.png",
        ITEM_DESC_KEY: "Lorem ipsum dolor sit\namet, consectetur."
    },
    {
        ITEM_IMAGE_KEY: f"{ITEMS_FILE_PATH}belt_of_strength.png",
        ITEM_DESC_KEY: "Lorem ipsum dolor sit\namet, consectetur."
    },
    {
        ITEM_IMAGE_KEY: f"{ITEMS_FILE_PATH}quelling_blade.png",
        ITEM_DESC_KEY: "Lorem ipsum dolor sit\namet, consectetur."
    },
    {
        ITEM_IMAGE_KEY: f"{ITEMS_FILE_PATH}boots_of_speed.png",
        ITEM_DESC_KEY: "Lorem ipsum dolor sit\namet, consectetur."
    },
    {
        ITEM_IMAGE_KEY: f"{ITEMS_FILE_PATH}ogre_axe.png",
        ITEM_DESC_KEY: "Lorem ipsum dolor sit\namet, consectetur."
    }
]


# The paths to each of the hero's item references
ITEMS_REFERENCES_TWO = [
    f"{REFERENCES_FILE_PATH}aaaa3.png",
    f"{REFERENCES_FILE_PATH}aaaa2.png",
    f"{REFERENCES_FILE_PATH}aaaa.png",
    f"{REFERENCES_FILE_PATH}aaaa5.png",
    f"{REFERENCES_FILE_PATH}aaaa6.png",
    f"{REFERENCES_FILE_PATH}aaaa7.png"
]
