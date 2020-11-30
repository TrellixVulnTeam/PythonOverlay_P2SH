"""
    main depends on detector, GUI, config, and hero setting files
"""
from GUI import navigator, hero
from detector import detector, ground_truth, processor
from config import GROUND_TRUTH_FILE_PATH, VIDEO_FILE_PATH
from hero_settings.hero_one import HERO_AVATAR_ONE, ITEMS_ONE, \
    ITEMS_REFERENCES_ONE, HERO_REFERENCE_ONE, ITEMS_ACCEPTABLE_ONE
from hero_settings.hero_two import HERO_AVATAR_TWO, ITEMS_TWO, \
    ITEMS_REFERENCES_TWO, HERO_REFERENCE_TWO, ITEMS_ACCEPTABLE_TWO
from hero_settings.hero_three import HERO_AVATAR_THREE, ITEMS_THREE, \
    ITEMS_REFERENCES_THREE, HERO_REFERENCE_THREE, ITEMS_ACCEPTABLE_THREE


if __name__ == '__main__':
    # read ground truth from file path
    ground_truth = ground_truth.GroundTruth(GROUND_TRUTH_FILE_PATH)

    # create heroes
    heroes = [hero.Hero(HERO_AVATAR_ONE, ITEMS_ONE, ITEMS_REFERENCES_ONE, HERO_REFERENCE_ONE, ITEMS_ACCEPTABLE_ONE),
              hero.Hero(HERO_AVATAR_TWO, ITEMS_TWO, ITEMS_REFERENCES_TWO, HERO_REFERENCE_TWO, ITEMS_ACCEPTABLE_TWO),
              hero.Hero(HERO_AVATAR_THREE, ITEMS_THREE, ITEMS_REFERENCES_THREE, HERO_REFERENCE_THREE, ITEMS_ACCEPTABLE_THREE)]

    # create navigator using the heroes
    navigator = navigator.Navigator(heroes)

    # create processor
    processor = processor.Processor(VIDEO_FILE_PATH)
    processor.start_async({detector.ARGS_PAGE_KEY: navigator.get_item_suggestions_page(),
                           detector.ARGS_GT_KEY: ground_truth, detector.ARGS_REF_KEY: []})

    # run the navigator
    navigator.run()

    # if the navigator is done running
    # disable the processor to kill the application
    processor.is_active = False
