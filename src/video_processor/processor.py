from cv2 import VideoCapture, waitKey, imshow, destroyWindow, CAP_PROP_FPS, CAP_PROP_FRAME_COUNT


class VideoProcessor:

    __PREVIEW_WIN_TITLE = "Current frame"
    __ERROR_OPENING_FRAME = "Error opening video stream or file"
    __EXIT_COMMAND = 'q'

    frame_before_callback = 30
    is_running = False
    force_stop = False

    def __init__(self, file_path):
        self.file_path = file_path

    def run(self, callback, before_show, args):
        video = VideoCapture(self.file_path)
        fps = video.get(CAP_PROP_FPS)

        if not video.isOpened():
            print(self.__ERROR_OPENING_FRAME)
        else:
            self.is_running = True
            frame_counter, n_frames = self.frame_before_callback, 0
            i = 0
            while video.isOpened() and not self.force_stop:
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
