import paddle
import os
import sys

sys.path.insert(0, os.getcwd())
from ppgan.apps import AnimeGANPredictor
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_image", type=str, help="path to source image")
    
    parser.add_argument("--output_path",
                        type=str,
                        default='output_dir',
                        help="path to output image dir")
    
    parser.add_argument("--weight_path",
                        type=str,
                        default=None,
                        help="path to model checkpoint path")
    
    parser.add_argument("--use_adjust_brightness",
                        action="store_false",
                        help="adjust brightness mode.")
    
    parser.add_argument("--cpu",
                        dest="cpu",
                        action="store_true",
                        help="cpu mode.")
    
    args = parser.parse_args()
    
    if args.cpu:
        paddle.set_device('cpu')
    
    predictor = AnimeGANPredictor(args.output_path, args.weight_path,
                                  # args.use_adjust_brightness)
                                  True)
    # predictor.run(args.input_image)
    
    # for AI creation 1th
    import cv2
    
    video_src = '/home/kohou/cvgames/interest/contest/baidu/AIstudio/AICreation/1th/data/videos/LiYunLong/handled/格式工厂混流 亮剑-03+亮剑-03+亮剑-04 00_00_23-.mp4'
    video_ = cv2.VideoCapture(video_src)
    video_name_ = os.path.basename(video_src)
    total_frames = video_.get(cv2.CAP_PROP_FRAME_COUNT)
    fps_ = video_.get(cv2.CAP_PROP_FPS)
    print("video {}, fps:{}, total frames:{}...".format(video_name_, fps_, total_frames))
    frame_count_ = 0
    save_per_frames = 1
    dst_dir = '/home/kohou/cvgames/interest/contest/baidu/AIstudio/AICreation/1th/data/videos/LiYunLong/handled/'
    
    out_video = cv2.VideoWriter('{}/hayao_{}'.format(dst_dir, video_name_),
                                cv2.VideoWriter_fourcc(*'DIVX'), int(fps_),
                                (int(video_.get(3)), int(video_.get(4))))
    while True:
        ret_, frame_ = video_.read()
        if not ret_:  # or len(fps_list_) == 0:
            break
        
        result_frame = predictor.anime_image_only(frame_)
        if frame_count_ % save_per_frames == 0:
            out_video.write(result_frame)
        frame_count_ = frame_count_ + 1
        if frame_count_ % 100 == 0:
            print("{}/{} processed...".format(frame_count_, int(total_frames)), flush=False)
