from detector.processor import Processor
from detector.ground_truth import GroundTruth
from GUI.navigator import Navigator
from GUI.hero import Hero


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
    item_refs_path = [
        "aaaa3.png",
        "aaaa2.png",
        "aaaa.png",
        "aaaa5.png",
        "aaaa6.png",
        "aaaa7.png"
    ]

    for i in range(0, len(items)):
        items[i]['image'] = prefix + items[i]['image']
        item_refs_path[i] = prefix + item_refs_path[i]

    under_lord = Hero('assets/images/heroes/underlord.png', items, item_refs_path)
    anti_mage = Hero('assets/images/heroes/anti_mage.png', items, item_refs_path)
    shadow_shaman = Hero('assets/images/heroes/shadow_shaman.png', items, item_refs_path)

    heroes = [under_lord, anti_mage, shadow_shaman]

    n = Navigator(heroes)

    args = {
        'page': n.get_item_suggestions_page(),
        'ground_truth': gt,
        'references': []
    }

    video_processor = Processor('assets/videos/replays/sample_test.mov')
    video_processor.frames_before_check = 30  # for debugging
    video_processor.start_async(args)

    n.run()

    video_processor.is_active = False




