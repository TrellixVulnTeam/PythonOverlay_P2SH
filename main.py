from video_processor.processor import VideoProcessor
from detector.reference import Reference
from detector import detector
from cv2 import imread, imshow, waitKey
from GUI.navigator import Navigator
from GUI.sub_pages.hero_select import HeroSelect
from GUI.hero import Hero

if __name__ == '__main__':

    prefix = "assets/images/items/"
    items = ["quelling_blade.png", "belt_of_strength.png",
             "crown.png", "boots_of_speed.png", "chainmail.png",
             "ogre_axe.png"]
    for i in range(0, len(items)):
        items[i] = prefix + items[i]

    under_lord = Hero('assets/images/heroes/underlord.png', items)
    anti_mage = Hero('assets/images/heroes/anti_mage.png', items)
    shadow_shaman = Hero('assets/images/heroes/shadow_shaman.png', items)

    heroes = [under_lord, anti_mage, shadow_shaman]

    n = Navigator(HeroSelect, heroes)
    n.run()
    #references = [Reference(imread('assets/images/items/4.png'))]

    #videoProcessor = VideoProcessor('assets/videos/replays/recording_01.mov')
    #videoProcessor.frame_before_callback = 1  # for debugging
    #videoProcessor.run(detector.frame_check, detector.after_frame_check, references)

