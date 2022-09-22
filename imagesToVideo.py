import os
import random
from moviepy import editor
from utils import resize, get_path

def images_to_video(video_name):
    global resize_path, logo_path, link_path, subs_path, video_path, sound_path

    video = get_path(video_path, video_name) + ".mp4"
    images = [get_path(resize_path, img) for img in os.listdir(resize_path)]
    clips = [editor.ImageClip(m).set_duration(10) for m in images]

    
    sound = editor.AudioFileClip(sound_path)
    audio_clip = sound.subclip(t_end=59.00)
    audio_sound = editor.CompositeAudioClip([audio_clip])

    logo = editor.ImageClip(logo_path)
    logo = logo.set_duration(59.00)
    logo = logo.resize(height=332, width=900)
    logo = logo.set_position(("center", 0.15))

    link = editor.ImageClip(link_path)
    link = link.resize(height=332, width=1000)
    link = link.set_position(("center", 0.80), relative=True)
    link = link.set_start((0, 45))
    link = link.set_duration(5)
    link = link.crossfadein(0.5)
    link = link.crossfadeout(0.5)

    subs = editor.ImageClip(subs_path)
    subs = subs.resize(height=332, width=900)
    subs = subs.set_position(("center", 0.80), relative=True)
    subs = subs.set_start((0, 51))
    subs = subs.set_duration(7)
    subs = subs.crossfadein(0.5)
    subs = subs.crossfadeout(0.5)

    movie_clip = editor.concatenate_videoclips(clips, method="compose")
    movie_clip.audio = audio_sound

    final = editor.CompositeVideoClip([movie_clip, logo, link, subs])
    final.write_videofile(video, fps=24)

    final.close()



video_path = get_path("vids")
img_path = get_path("img")

sound_folder = get_path("sounds")
sounds = [file for file in os.listdir(sound_folder)]
sound_path = get_path(sound_folder, random.choice(sounds))

resize_path = get_path("resize")
logo_path =  get_path("features", "logo.png")
link_path  =  get_path("features", "Link in description.png")            
subs_path = get_path("features", "like&subscribe.png")           

if __name__ == "__main__":
    video_name = "test11_final"
    resize(img_path)
    images_to_video(video_name)



