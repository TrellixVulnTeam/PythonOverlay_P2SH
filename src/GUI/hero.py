

ITEM_IMAGE_KEY = 'image'
ITEM_DESC_KEY = 'desc'
ITEM_DESC_NAME = 'name'


class Hero:
    """
        Hero is used to create an object that can be selected within
        the hero select page containing each hero's specific properties
    """

    def __init__(self, avatar_image_path,
                 item_images, item_images_ref_path, avatar_reference_path,
                 min_acceptable_matches=10):
        # The path to the hero's avatar image
        self.avatar_image_path = avatar_image_path
        # A list of path to small variations of each item image
        # and a description of those items
        self.item_images = item_images
        # A list of the file path to each items reference image
        self.item_images_ref_path = item_images_ref_path
        self.avatar_reference_path = avatar_reference_path
        self.min_acceptable_matches = min_acceptable_matches




