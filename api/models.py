from django.db import models


class Job(models.Model):
    """ Images """
    job_image = models.ImageField(upload_to='images/')

class History(models.Model):
    """ Processing history of each image """

    BLACK_AND_WHITE = 'black_and_white'
    INVERT_COLORS = 'invert_colors'
    INVERT_ON_AXIS = 'invert_on_axis'
    ROTATE = 'rotate'

    STEP_CHOICES = [
        (BLACK_AND_WHITE, 'Black and white'),
        (INVERT_COLORS, 'Invert colors'),
        (INVERT_ON_AXIS, 'Invert on y axis'),
        (ROTATE, 'Rotate 90°')
        ]

    step = models.CharField(max_length=20, choices=STEP_CHOICES)
    date = models.DateTimeField(auto_now_add=True)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return f'Job id:{self.job_id}\nStep: {self.step}\nDate: {self.date}'

