import os
import math
import random
from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip


def get_bounce_pos(t, start, velocity, max_val):
    """
    根據時間 t 計算在 [0, max_val] 區間內的反彈位置。
    利用鏡像法則，讓物件碰到邊緣時反向移動。
    """
    pos = start + velocity * t
    period = 2 * max_val
    pos_mod = pos % period
    if pos_mod > max_val:
        return period - pos_mod
    else:
        return pos_mod


# 設定來源及輸出目錄
src_folder = "src"
build_folder = "build"
if not os.path.exists(build_folder):
    os.makedirs(build_folder)

# 水印圖片檔案路徑
watermark_path = "watermark.png"

# 設定水印移動速度（單位：像素/秒）
speed = 100

# 遍歷 src 目錄中的所有 MP4 影片
for filename in os.listdir(src_folder):
    if filename.lower().endswith(".mp4"):
        video_path = os.path.join(src_folder, filename)
        output_path = os.path.join(build_folder, filename)

        # 讀取影片
        video = VideoFileClip(video_path)
        # 讀取水印圖片並設定持續時間與影片相同
        wm = ImageClip(watermark_path).set_duration(
            video.duration).set_opacity(0.2)

        # 取得影片與水印的尺寸
        video_width, video_height = video.w, video.h
        wm_width, wm_height = wm.w, wm.h

        # 計算水印可移動的最大範圍（確保整個水印圖片都在影片內）
        max_x = video_width - wm_width
        max_y = video_height - wm_height

        # 初始位置設定為中央位置
        start_x = max_x / 2
        start_y = max_y / 2

        # 以隨機角度決定初始方向
        angle = random.uniform(0, 2 * math.pi)
        vx = speed * math.cos(angle)
        vy = speed * math.sin(angle)

        # 設定水印位置：利用 lambda 函式傳回 (x, y) 座標
        wm = wm.set_pos(lambda t: (get_bounce_pos(t, start_x, vx, max_x),
                                   get_bounce_pos(t, start_y, vy, max_y)))

        # 合成影片與水印
        final = CompositeVideoClip([video, wm])
        # 將結果輸出，預設編碼器為 libx264
        final.write_videofile(output_path, codec="libx264")
