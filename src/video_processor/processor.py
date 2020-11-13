from cv2 import VideoCapture, waitKey, imshow


class VideoProcessor:

    __PREVIEW_WIN_TITLE = "Current frame"
    __ERROR_OPENING_FRAME = "Error opening video stream or file"
    __EXIT_COMMAND = 'q'

    frame_before_callback = 30

    def __init__(self, file_path):
        self.file_path = file_path

    def run(self, callback, before_show, args):
        video = VideoCapture(self.file_path)
        if not video.isOpened():
            print(self.__ERROR_OPENING_FRAME)
        else:
            frame_counter = self.frame_before_callback
            while video.isOpened():
                ret, frame = video.read()

                if not ret or waitKey(1) & 0xFF == ord(self.__EXIT_COMMAND):
                    break
                else:
                    frame_counter += 1

                    if frame_counter >= self.frame_before_callback:
                        frame_counter = 0
                        callback(frame, args)

                    before_show(frame, args)
                    imshow(self.__PREVIEW_WIN_TITLE, frame)

        video.release()
