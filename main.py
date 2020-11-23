from detector.processor import Processor
from GUI.navigator import Navigator
from GUI.sub_pages.hero_select import HeroSelect
from GUI.sub_pages.item_suggestions import ItemSuggestions
from GUI.hero import Hero
from detector.ground_truth import GroundTruth


if __name__ == '__main__':

    gt = GroundTruth('assets/csv/sample.csv')

    txt = "Lorem ipsum dolor sit\namet, consectetur."
    prefix = "assets/images/items/"
    items = [
        {'image': "chainmail.png", 'desc': txt},
        {'image': "crown.png", 'desc': txt},
        {'image': "belt_of_strength.png", 'desc': txt},
        {'image': "quelling_blade.png", 'desc': txt},
        {'image': "boots_of_speed.png", 'desc': txt},
        {'image': "ogre_axe.png", 'desc': txt}
    ]
    item_refs = [
        "aaaa3.png",
        "aaaa2.png",
        "aaaa.png",
        "aaaa5.png",
        "aaaa6.png",
        "aaaa7.png"
    ]

    for i in range(0, len(items)):
        items[i]['image'] = prefix + items[i]['image']
        item_refs[i] = prefix + item_refs[i]

    under_lord = Hero('assets/images/heroes/underlord.png', items, item_refs)
    anti_mage = Hero('assets/images/heroes/anti_mage.png', items, item_refs)
    shadow_shaman = Hero('assets/images/heroes/shadow_shaman.png', items, item_refs)

    heroes = [under_lord, anti_mage, shadow_shaman]

    n = Navigator(HeroSelect, heroes)

    sub_pages = n.get_sub_pages()
    item_suggestions = [x for x in sub_pages if type(x) is ItemSuggestions][0]

    args = {
        'page': item_suggestions,
        'ground_truth': gt,
        'references': []
    }

    video_processor = Processor('assets/videos/replays/sample_test.mov')
    video_processor.frame_before_callback = 30  # for debugging
    video_processor.start_async(args)

    n.run()




