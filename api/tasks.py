from PIL import Image, ImageOps
from datetime import datetime
from timeit import default_timer as timer
from .models import History


class Tasks():
    """ All possible image processes """

    def __init__(self, image_filename):
        self.image_filename = image_filename

    def invert_colors(self):
        """  """
        with Image.open(self.image_filename).convert('RGB') as image:
            inverted_image = ImageOps.invert(image)
            inverted_image.save(self.image_filename)


    def black_and_white(self):
        """  """

        with Image.open(self.image_filename).convert('RGB') as image:
            bw_image = image.convert('L')
            bw_image.save(self.image_filename)


    def rotate(self):
        """  """

        with Image.open(self.image_filename).convert('RGB') as image:
            rotated_image = image.rotate(90, expand=True)
            rotated_image.save(self.image_filename)


    def invert_on_axis(self):
        """"  """

        with Image.open(self.image_filename).convert('RGB') as image:
            flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
            flipped_image.save(self.image_filename)