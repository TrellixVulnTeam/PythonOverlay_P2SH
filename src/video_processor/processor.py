from cv2 import VideoCapture, waitKey, imread, imshow, destroyWindow, CAP_PROP_FPS, CAP_PROP_FRAME_COUNT, cvtColor, \
    COLOR_RGB2GRAY, COLOR_RGB2BGR
from numpy import array, uint8
from PIL import ImageGrab


def get_screenshot():
    image = ImageGrab.grab()
    image = cvtColor(array(image, uint8), COLOR_RGB2BGR)
    return image


class VideoProcessor:
    __PREVIEW_WIN_TITLE = "Current frame"
    __ERROR_OPENING_FRAME = "Error opening video stream or file"
    __EXIT_COMMAND = 'q'

    frame_before_callback = 30
    is_running = False
    force_stop = False

    def __init__(self, file_path):
        self.file_path = file_path

    def run_screen(self, callback, before_show, args):
        self.is_running = True
        frame_counter, n_frames, i = self.frame_before_callback, 0, 0
        while not self.force_stop:
            frame_counter += 1

            if frame_counter >= self.frame_before_callback:
                frame_counter = 0
                frame = get_screenshot()
                callback(frame, args, i, current_duration=1)
                before_show(frame, args)
                imshow(self.__PREVIEW_WIN_TITLE, frame)
                waitKey(1)

        self.is_running = False

    def run_video(self, callback, before_show, args):
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
                        callback(frame, args, i, current_duration)

                    before_show(frame, args)
                    imshow(self.__PREVIEW_WIN_TITLE, frame)
                i += 1

        destroyWindow(self.__PREVIEW_WIN_TITLE)
        self.is_running = False
        self.force_stop = False
        video.release()
