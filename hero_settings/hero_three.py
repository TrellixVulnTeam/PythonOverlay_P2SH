"""
    hero three depends on key values from GUI.HERO and hero settings
    It defines avatar, item and references file paths for hero three
"""
from GUI.hero import ITEM_DESC_KEY, ITEM_IMAGE_KEY, ITEM_DESC_NAME
from config import ITEMS_FILE_PATH, REFERENCES_FILE_PATH


# The path to the hero's avatar image
HERO_AVATAR_THREE = 'assets/images/heroes/shadow_shaman.png'

# The path to the hero's reference image
HERO_REFERENCE_THREE = 'assets/images/heroes/shadow_shaman_reference.png'


# The paths and description of each of the hero's items
ITEMS_THREE = [
    {
        ITEM_IMAGE_KEY: f"{ITEMS_FILE_PATH}robe_of_the_magi.png",
        ITEM_DESC_NAME: "Robe of the Magi",
        ITEM_DESC_KEY: "This robe corrupts the soul of the user, but\nprovides wisdom in return. (+6 Intelligence) ("
                       "450 gold) "
    },
    {
        ITEM_IMAGE_KEY: f"{ITEMS_FILE_PATH}mantle_of_intelligence.png",
        ITEM_DESC_NAME: "Mantle of Intelligence",
        ITEM_DESC_KEY: "A beautiful sapphire mantle worn by\ngenerations of queens. (+3 Intelligence) (145 gold)"
    },
    {
        ITEM_IMAGE_KEY: f"{ITEMS_FILE_PATH}sage's_mask.png",
        ITEM_DESC_NAME: "Sage's mask",
        ITEM_DESC_KEY: "A mask commonly used by mages and warlocks for\nvarious rituals. (+0.6 Mana regeneration) ("
                       "175 gold) "
    },
    {
        ITEM_IMAGE_KEY: f"{ITEMS_FILE_PATH}ring_of_protection.png",
        ITEM_DESC_NAME: "Ring of Protection",
        ITEM_DESC_KEY: "A glimmering ring that defends its bearer.\n(+2 Armor) (175 gold)"
    },
    {
        ITEM_IMAGE_KEY: f"{ITEMS_FILE_PATH}broadsword.png",
        ITEM_DESC_NAME: "Broadsword",
        ITEM_DESC_KEY: "The classic weapon of choice for knights, this blade is\nsturdy and reliable for slaying "
                       "enemies. (+15 Attack damage) (1000 gold) "
    },
    {
        ITEM_IMAGE_KEY: f"{ITEMS_FILE_PATH}staff_of_wizardry.png",
        ITEM_DESC_NAME: "Staff of Wizardry",
        ITEM_DESC_KEY: "A staff of magical powers passed down from\nthe eldest mages. (+10 Intelligence) (1000 gold)"
    }
]


# The paths to each of the hero's item references
ITEMS_REFERENCES_THREE = [
    f"{REFERENCES_FILE_PATH}robe_of_the_magi.png",
    f"{REFERENCES_FILE_PATH}mantle_of_intelligence.png",
    f"{REFERENCES_FILE_PATH}sage's_mask.png",
    f"{REFERENCES_FILE_PATH}ring_of_protection.png",
    f"{REFERENCES_FILE_PATH}broadsword.png",
    f"{REFERENCES_FILE_PATH}staff_of_wizardry.png"
]


ITEMS_ACCEPTABLE_THREE = [
    10,
    10,
    10,
    10,
    12,
    10
]
