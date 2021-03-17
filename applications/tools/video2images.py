# -*- coding: utf-8 -*-

__author__ = 'kohou.wang'
__time__ = '3/16/21'
__email__ = 'oukohou@outlook.com'

# If this runs wrong, don't ask me, I don't know why;
# If this runs right, thank god, and I don't know why.
# Maybe the answer, my friend, is blowing in the wind.
# Well, I'm kidding... Always, Welcome to contact me.

"""Description for the script:

"""

import cv2
import os

def video2images(video_source_, dst_dir_, save_per_seconds_=2):
    video_ = cv2.VideoCapture(video_source_)
    
    video_name_ = os.path.basename(video_source_)
    dst_sub_path = dst_dir_
    if not os.path.exists(dst_sub_path):
        os.makedirs(dst_sub_path)
    
    total_frames = video_.get(cv2.CAP_PROP_FRAME_COUNT)
    fps_ = video_.get(cv2.CAP_PROP_FPS)
    print("video {}, fps:{}...".format(video_name_, fps_))
    
    save_per_frames = int(save_per_seconds_ * fps_)
    frame_count_ = 0
    while True:
        ret_, frame_ = video_.read()
        if not ret_:  # or len(fps_list_) == 0:
            break
        
        if frame_count_ % save_per_frames == 0:
            cv2.imwrite(os.path.join(dst_sub_path, "{}_{}.png".format(".".join(video_name_.split('.')[:-1]), frame_count_)),
                        frame_)
        frame_count_ = frame_count_ + 1
        if frame_count_ % 1000 == 0:
            print("{}/{} processed...".format(frame_count_, int(total_frames)), flush=False)


if __name__ == "__main__":
    video2images('/home/kohou/cvgames/interest/contest/baidu/AIstudio/AICreation/1th/data/videos/LiYunLong/handled/《亮剑》 第3集 00_24_48-00_26_34.mp4',
                 '/home/kohou/cvgames/interest/contest/baidu/AIstudio/AICreation/1th/data/images/li',
                 1)
