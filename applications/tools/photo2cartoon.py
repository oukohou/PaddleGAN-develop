# -*- coding: utf-8 -*-

__author__ = 'kohou.wang'
__time__ = '3/17/21'
__email__ = 'oukohou@outlook.com'

# If this runs wrong, don't ask me, I don't know why;
# If this runs right, thank god, and I don't know why.
# Maybe the answer, my friend, is blowing in the wind.
# Well, I'm kidding... Always, Welcome to contact me.

"""Description for the script:

"""
from ppgan.apps import Photo2CartoonPredictor

p2c = Photo2CartoonPredictor(output_path='/home/kohou/cvgames/interest/contest/baidu/AIstudio/AICreation/1th/data/images/li')
p2c.run('/home/kohou/cvgames/interest/contest/baidu/AIstudio/AICreation/1th/data/images/li/《亮剑》 第3集 00_24_48-00_26_34_2425.png')
# p2c.cartoon_only('/home/kohou/cvgames/interest/contest/baidu/AIstudio/AICreation/1th/data/images/li/《亮剑》 第3集 00_24_48-00_26_34_800.png')
if __name__ == "__main__":
    pass
