from string import ascii_letters
import textwrap, requests, io
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

import imageGraber, quoteGraber
from utils import ImageWriter

class TextOnImage:
    """ 
        A simple utility class that will allow the writting of the texts(quotes) to the image
        An issue i faced here waas the resizing of the image to fit instagram image standard (1080 x 1080) 
        I achieved to reached a 100,80 % ration on the sizing using the resampling .BICUBIC method
        I also had to darken the image a bit so the text could be more pleasing to read. 
    """

    def __init__(self, image: Image, text ):
        """ 
            The init of this class takes the following:
            image: Image, a pillow image type
            text:dict, the quote we are to write, of type dict as i found it was easier to manipulate  
        """
        image.thumbnail((720, 1080), Image.Resampling.HAMMING)
        enhancer = ImageEnhance.Brightness(image)
        self.image = enhancer.enhance(0.5)
        self.text = text
        self.draw = ImageDraw.Draw(self.image)

    def draw_text(self, scale=.95, color="white"):
        """ 
            The draw_text function takes in as parameter:
            scale: float, Easily scale the text to fit on image where 1 refers to full scale (fit image completely)
            color: str, using Pillow image attribute to set the font color
        """
        font = ImageFont.truetype("Poppins-Black.ttf",50)
        avg_char_width = sum(font.getlength(char) for char in ascii_letters) / len(ascii_letters)
        max_char_count = int((self.image.size[0] * scale ) /avg_char_width)
        message = textwrap.fill(self.text[0].get("text"), max_char_count)
        final_message = message + '\n\n' + self.text[0].get("author")

        position = (self.image.size[0]/2, self.image.size[1]/2)

        self.draw.text(
            xy=(position[0], position[1]),
            text=final_message,
            font=font,
            fill=color,
            anchor="mm"
        )
    

    def show(self):

        self.image.show()
    
    def save_file(self, name):
        final_name = "[MOD] " + name
        final = ImageWriter(final_name, self.image)
        final.write()

def create_image(term, show=False, save=True):
    image_dict = imageGraber.image_graber(term)
    
    quote = quoteGraber.grab_quote(term, 1)
    text = quote[0].get('text')

    # gets an image that's not longer than 200 words
    while len(text) >= 200:
        quote = quoteGraber.grab_quote(term, 1)
        text = quote[0].get('text')

    file_name = image_dict[0]['id']
    img_page = requests.get(image_dict[0]['url']).content
    img = Image.open(io.BytesIO(img_page))
    image = TextOnImage(img, quote)
    image.draw_text()

    if show:
        image.show()
    
    if save:
        image.save_file(file_name)


if __name__ == "__main__":
    term = 'motivation'
    for i in range(6):
        create_image(term)