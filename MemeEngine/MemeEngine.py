"""Meme Engine writes quotes on images and stores back."""


from PIL import Image, ImageDraw, ImageFont
import random
import os


class MemeEngine:
    """Write quote on an image."""

    def __init__(self, output_dir: str):
        """Construct the class and make directories."""
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.mkdir(self.output_dir)

    def make_meme(self, img_path: str, text: str, author: str, width=500):
        """Generate the meme and stores it on a user specified location."""
        try:
            with Image.open(img_path) as img:
                ratio = width / float(img.size[0])
                height = int(ratio * float(img.size[1]))

                img = img.resize((width, height))

                draw = ImageDraw.Draw(img)

                font_path = os.path.normpath('./font/Open_Sans/OpenSans-VariableFont_wdth,wght.ttf')
                font = ImageFont.truetype(font_path, 20)

                loc = (60, random.randint(30, img.size[0] - 50))
                draw.text(loc, text, font=font, fill='yellow')

                draw.text(loc, '\n- ' + author, font=font, fill='white')

                out_file = str(random.randint(1, 1000)) + '.png'
                img.save(os.path.normpath(self.output_dir + '/' + out_file))
                return os.path.normpath(self.output_dir + '/' + out_file)
        except:
            raise Exception('Image Path is not valid.')
