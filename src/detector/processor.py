from cv2 import VideoCapture, waitKey, imread, imshow, destroyWindow, CAP_PROP_FPS, cvtColor, COLOR_RGB2BGR
from numpy import array, uint8
from PIL import ImageGrab
from time import sleep
from threading import Thread
from detector.detector import frame_check, after_frame_check
from detector.reference import Reference

def get_screenshot():
    image = ImageGrab.grab()
    image = cvtColor(array(image, uint8), COLOR_RGB2BGR)
    return image


class Processor:
    __PREVIEW_WIN_TITLE = "Current frame"
    __ERROR_OPENING_FRAME = "Error opening video stream or file"
    __EXIT_COMMAND = 'q'

    frame_before_callback = 30
    is_running = False
    force_stop = False

    def __init__(self, file_path):
        self.file_path = file_path

    def start_async(self, args):
        thread = Thread(target=self.start, args=(args,))
        thread.start()

    def start(self, args):
        page = args['page']
        while True:
            if page.is_active and page.last_hero is not None and not self.is_running:
                roi = (0, 0, 0, 0)
                color = (0, 255, 0)
                args['references'] = []
                for item_image in page.last_hero.item_images_ref:
                    args['references'].append(Reference(imread(item_image), roi, color))

                t = Thread(target=self.__listen_for_stop_detection, args=(page, args['ground_truth']))
                t.start()

                if self.file_path is None:
                    self.__run_screen(args)
                else:
                    self.__run_video(args)
            else:
                sleep(1)

    def __listen_for_stop_detection(self, page, ground_truth):
        while not self.force_stop:
            sleep(1)
            if not page.is_active and self.is_running:
                self.force_stop = True
                ground_truth.save('assets/csv/result.csv')
                ground_truth.reset()

    def __run_screen(self, args):
        # The ROI of the target image, that should be matched
        args['roi'] = (0, 0, 0, 0)
        self.is_running = True
        frame_counter, n_frames, i = self.frame_before_callback, 0, 0
        while not self.force_stop:
            frame_counter += 1

            if frame_counter >= self.frame_before_callback:
                frame_counter = 0
                frame = get_screenshot()
                frame_check(frame, args, i, False, current_duration=1)
                after_frame_check(frame, args)
                imshow(self.__PREVIEW_WIN_TITLE, frame)
                waitKey(1)

        self.is_running = False

    def __run_video(self, args):
        # The ROI of the target image, that should be matched
        args['roi'] = (930, 35, 1084, 630)

        video = VideoCapture(self.file_path)
        fps = video.get(CAP_PROP_FPS)

        if not video.isOpened():
            print(self.__ERROR_OPENING_FRAME)
        else:
            self.is_running = True
            frame_counter, n_frames, i = self.frame_before_callback, 0, 0
            while not self.force_stop:

                ret, frame = video.read()

                if not ret or self.force_stop or waitKey(1) & 0xFF == ord(self.__EXIT_COMMAND):
                    break
                else:
                    frame_counter += 1
                    n_frames += 1

                    if frame_counter >= self.frame_before_callback:
                        current_duration = float(n_frames) / float(fps)
                        frame_counter = 0
                        frame_check(frame, args, i, True, current_duration)

                    after_frame_check(frame, args)
                    imshow(self.__PREVIEW_WIN_TITLE, frame)
                i += 1

        destroyWindow(self.__PREVIEW_WIN_TITLE)
        self.is_running = False
        self.force_stop = False
        video.release()
