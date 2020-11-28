"""
    The processor depends on cv2, numpy, PIL, time, threading, Reference and detector
"""
from cv2 import VideoCapture, waitKey, imread, imshow, destroyWindow, \
    cvtColor, CAP_PROP_FPS, COLOR_RGB2BGR
from numpy import array, uint8
from PIL import ImageGrab
from time import sleep
from threading import Thread
from GUI.sub_pages.hero_select import HeroSelect
from detector.detector import frame_check, after_frame_check, \
    ARGS_REF_KEY, ARGS_PAGE_KEY, ARGS_ROI_KEY, ARGS_GT_KEY
from detector.reference import Reference


# The title of the cv2 window displaying target images
PREVIEW_WIN_TITLE = "Current frame"
# The error message displayed if the video is unable to open
ERROR_OPENING_FRAME = "Error opening video stream or file"

# The video's region of interest
VIDEO_ROI = (930, 35, 1084, 630)
# The reference's region of interest
REFERENCE_ROI = (0, 0, 0, 0)
# The reference's highlight color
REFERENCE_COLOR = (0, 255, 0)


def get_screenshot():
    """
       Returns an image of the primary monitor
    """
    image = ImageGrab.grab()
    image = cvtColor(array(image, uint8), COLOR_RGB2BGR)
    return True, image


class Processor:
    """
        The processor executes the detection processes either based on a real-time
        image or frames loaded from a video located at the file path
    """

    # Specify the number of frames which should pass
    # before running the detection check
    frames_before_check = 30

    # Determines if the processor is running
    is_running = False

    # Determines if the processor should stop
    force_stop = False

    def __init__(self, file_path):
        self.file_path = file_path
        self.is_active = True

    def start_async(self, args):
        """
            Start the detection process in a thread
        """
        thread = Thread(target=self.start, args=(args,))
        thread.start()

    def start(self, args):
        """
            Waits for the item suggestion page to specify a hero and being active
            before it executes the detection process
        """

        # get the page from args
        page = args[ARGS_PAGE_KEY]

        # specify args ROI
        args[ARGS_ROI_KEY] = VIDEO_ROI if self.file_path is not None else (0, 0, 0, 0)

        # run the detection while the processor object is active
        while self.is_active:

            # if the page is active and specify a last hero and is not already running
            if page.is_active and page.last_hero is not None and not self.is_running:
                # Set the processor as running to avoid executing this code block
                # when the processor is already running
                self.is_running = True

                # reset reference list to ensure it only consist of references for
                # the last selected hero
                args[ARGS_REF_KEY] = []

                # loop through the item images specified within the last selected hero
                for item_image_path in page.last_hero.item_images_ref_path:
                    # read the reference image
                    image = imread(item_image_path)
                    # create a reference
                    reference = Reference(image, REFERENCE_ROI, REFERENCE_COLOR)
                    # append the reference to the args reference list
                    args[ARGS_REF_KEY].append(reference)

                # Start the detection process against a real-time image or a video
                self.__run(args)
            else:
                sleep(1)

    def __run(self, args):
        """
            Loops through either every frame of the video specified at the file path
            or get a screenshot of the primary monitor and use the detection methods
            to check if any of the references specified in args is presence within
            the image
        """

        # Check if a file path was given
        # and save this info for later to
        # execute functionality only related
        # to processing videos
        use_video = self.file_path is not None

        # Set the frame count to the value of frames before check
        # to ensure to detect first time the while loop runs
        frame_counter = self.frames_before_check

        # n_frames is used to specify the actual number of frames
        # which have been passed at a given moment
        n_frames = 0

        # current duration is used to pass to the detection method
        # to find the ground truth data matching the current frame
        current_duration = 0

        # declare an empty object to reference the video object
        # that can be used if a file path was specified
        video, fps = None, None
        if use_video:
            # create a video capture object from the file path
            video = VideoCapture(self.file_path)
            fps = video.get(CAP_PROP_FPS)

            # stop the method if there is any problem opening the video
            # and warn the developer
            if not video.isOpened():
                print(ERROR_OPENING_FRAME)
                return

        # loop while force stop is False
        while not self.force_stop:

            # increase frame counter to execute the frame check
            # when it reaches the value of 'frames_before_check
            frame_counter += 1

            # keep track of the current number of frames to be
            # able to calculate the current duration
            n_frames += 1

            # get the current frame or a screenshot of the primary monitor
            ret, frame = video.read() if use_video else get_screenshot()

            # if the page specified within args is no longer active
            # or the processor is done processing the video
            if not args[ARGS_PAGE_KEY].is_active or not ret:

                # and, the processor is processing a video
                if use_video and args[ARGS_GT_KEY] is not None:
                    # save the results of the detection evaluation
                    args[ARGS_GT_KEY].save()
                    # and reset the values to be able to process
                    # the video or new real-time screenshots
                    args[ARGS_GT_KEY].reset()
                    # switch back to hero select page
                    if args[ARGS_PAGE_KEY].is_active:
                        args[ARGS_PAGE_KEY].on_click()
                # stop the while loop
                self.force_stop = True
                break

            # if the frame counter is greater than frames_before_check
            if frame_counter >= self.frames_before_check:
                # reset the frame counter to ensure this block of code
                # executes again after a specified number of frames
                frame_counter = 0

                # if the processor is processing a video
                if use_video:
                    # calculate the current duration of the video
                    current_duration = n_frames / fps

                # perform the frame check
                frame_check(frame, args, n_frames, use_video, current_duration)

            # execute after frame check functionality for every
            # frame to be able to show item matches in debugging
            after_frame_check(frame, args)

            # if the processor is processing a video
            if use_video:
                # display the video that is being processed
                imshow(PREVIEW_WIN_TITLE, frame)

            # add some delay
            waitKey(1)

        # Set is running and force stop to
        # false to ensure that new processes
        # can be started if another hero is
        # selected on the hero page
        self.is_running = False
        self.force_stop = False

        # if the processor is processing a video
        if use_video:
            # ensure to close the video showing the results
            destroyWindow(PREVIEW_WIN_TITLE)
            # and release the video capture
            video.release()
