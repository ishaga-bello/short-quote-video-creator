import os
from os.path import join, dirname, abspath
from dotenv import load_dotenv
from pyunsplash import PyUnsplash


dotenv_path = join(dirname(abspath("__file__")), './.env')
load_dotenv(dotenv_path)

UNSPLASH_ACCESS_KEY = os.environ.get("UNSPLASH_ACCESS_KEY")

def to_dict(image_object): 
    image = dict()
    image['id'] = image_object.id
    image['url'] = image_object.link_download
    return image


def image_graber(term, random=True, number_of_image=1):

    pu = PyUnsplash(api_key=UNSPLASH_ACCESS_KEY)


    if random:
        photos = pu.photos(type_='random', count=number_of_image, featured=True, query=term, orientation='portrait')
    
    else:
        photos = pu.search(type_='search', per_page=number_of_image, query=term)
    
    photo_list = [photo for photo in photos.entries]
    image = [to_dict(photo) for photo in photo_list]

    return image
    

