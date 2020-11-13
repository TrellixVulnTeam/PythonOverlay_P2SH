from video_processor.processor import VideoProcessor
from detector.reference import Reference
from detector import detector
from cv2 import imread, imshow, waitKey


if __name__ == '__main__':
    references = [Reference(imread('assets/images/items/4.png'))]

    videoProcessor = VideoProcessor('assets/videos/replays/recording_01.mov')
    videoProcessor.frame_before_callback = 1  # for debugging
    videoProcessor.run(detector.frame_check, detector.after_frame_check, references)

