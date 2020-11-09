from cv2 import imread, rectangle
from VideoProcessor.VideoProcessor import VideoProcessor
from Detector.DetectionMethod import DetectionMethod
from Detector.DetectionReference import DetectionReference
from Detector.ROI import ROI


def frame_check(frame):
    if not ref.match and ref.can_detect():
        # ref.async_detect(frame, method=DetectionMethod.BLOB_ANALYSIS)
        # for debugging
        ref.detect(frame, method=DetectionMethod.BLOB_ANALYSIS)


def after_frame_check(frame):
    if ref.match:
        rectangle(frame, ref.get_top_left(), ref.get_bottom_right(), color=150, thickness=2)


if __name__ == '__main__':
    # roi = ROI(y_start=945, y_end=45, x_start=1094, x_end=638)  # template matching ROI

    y_ranges, x_ranges = [(0,0)]*6, [(0,0)]*6
    y_ranges[0], x_ranges[0] = (945,100), (1098,770)
    y_ranges[1], x_ranges[1] = (945, 100), (1167, 704)
    y_ranges[2], x_ranges[2] = (945, 100), (1225, 638)
    y_ranges[3], x_ranges[3] = (995, 50), (1098, 770)
    y_ranges[4], x_ranges[4] = (995, 50), (1167, 704)
    y_ranges[5], x_ranges[5] = (995, 50), (1225, 638)

    roi = ROI(y_ranges, x_ranges)  # blob analysis ROI
    ref = DetectionReference(image=imread('assets/reference_images/f.png'), roi=roi)

    videoProcessor = VideoProcessor('assets/replays/sample_test.mov')
    videoProcessor.frame_before_callback = 5  # for debugging
    videoProcessor.run(frame_check, after_frame_check)
