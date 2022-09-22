import utils
from imagesToVideo import images_to_video
from textOnImage import create_image
from random import choice

term_list = ["love", "inspiration", "motivation", "power", "discipline"]

# nbr_of_videos = input(int("Enter the number of videos to be created"))
img_path = utils.get_path("img")
resize_path = utils.get_path("resize")
video_name = "final"

for number in range(1):
    term = choice(term_list)
    utils.clean(img_path)
    for i in range(6):
        create_image(term)

    utils.clean(resize_path)
    utils.resize(img_path)
    images_to_video(video_name)

