from moviepy.editor import VideoFileClip, clips_array
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import moviepy.video.fx.all as vfx

# Время начала вырезанного фрагмента в секундах
start_time = 10
# Время окончания вырезанного фрагмента в секундах
end_time = 30

# вырезаем фрагмент видео
def cut(input_m="movie/1.avi", output_m="ready/out.avi", duration_movie=0, count_movie=0):
    # Путь к видеофайлу
    video_path = input_m
    # Путь к выходному видеофайлу
    output_path = output_m

    # Открываем видеофайл
    video = VideoFileClip(video_path)

    # Получаем длительность видео в секундах
    duration = int(duration_movie)
    count = int(count_movie)

    # Вырезаем фрагмент видео
    ffmpeg_extract_subclip(video_path, start_time, end_time, targetname=output_path)

# Повернуть и изменить размеры видео
def redact(input_m="ready/out.avi", output_m="ready/out_1.avi"):
    # Путь к исходному видеофайлу
    video_path = input_m
    # Путь к выходному видеофайлу
    output_path = output_m

    # Загружаем видео
    video = VideoFileClip(video_path)

    # Поворачиваем видео на 90 градусов (по часовой стрелке)
    rotated_video = video.rotate(90)

    # Изменяем размер видео на 1080x1920
    resized_video = rotated_video.resize(height=1920)

    # Создаем черные полосы для подгонки видео к вертикальному формату
    black_bars = vfx.black_clip(resized_video, 1080, keep_duration=True)

    # Склеиваем видео с черными полосами
    final_video = clips_array([[resized_video.set_position('center')], [black_bars]])

    # Сохраняем видео
    final_video.write_videofile(output_path, fps=video.fps)


if __name__ == "__main__":
    redact()
# Выводим длительность видео
# print(duration)
# print(count)
