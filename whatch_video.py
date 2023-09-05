import os
import cv2
import NetWork4
from time import sleep

poses = NetWork4.get_poses()
# print(poses)

img = cv2.imread('video2/' + os.listdir('video2')[0])
# height, width, layers = img.shape
# video = cv2.VideoWriter("our_video.mp4", 0, 1, (height, width))

for n, el in enumerate(os.listdir('video2')):
    frame = cv2.imread('video2/' + el)

    # describe the type of font
    # to be used.
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Use putText() method for
    # inserting text on videos


    cv2.putText(frame,
                f'{poses[n]}',
                (100, 100),
                font, 3,
                (0, 255, 255),
                2,
                cv2.LINE_4)


    w, h = frame.shape[:2]
    down_points = (int(h * 0.5), int(w * 0.5))
    frame = cv2.resize(frame, down_points, interpolation=cv2.INTER_LINEAR)


    cv2.imshow('video', frame)
    # sleep(3)йййй
    # creating 'q' as the quit
    # button for the videoqq
    cv2.waitKey(0)
    # sleep(0.5)

    # video.write(frame)

    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

# video.release()



#
# image_folder = '.'  # make sure to use your folder
# video_name = 'mygeneratedvideo.avi'
#
# images = [img for img in os.listdir(image_folder)
#           if img.endswith(".jpg") or
#           img.endswith(".jpeg") or
#           img.endswith("png")]
#
# # Array images should only consider
# # the image files ignoring others if any
# print(images)
#
# frame = cv2.imread(os.path.join(image_folder, images[0]))
#
# # setting the frame width, height width
# # the width, height of first image
# height, width, layers = frame.shape
#
# video = cv2.VideoWriter(video_name, 0, 1, (width, height))
#
# # Appending the images to the video one by one
# for image in images:
#     video.write(cv2.imread(os.path.join(image_folder, image)))
#
#     # Deallocating memories taken for window creation
# cv2.destroyAllWindows()
# video.release()
