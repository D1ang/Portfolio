from django.db import models


class VideoItem(models.Model):
    """
    A model for the video items.
    """
    title = models.CharField(max_length=50, blank=False, null=False)
    source = models.URLField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='videos', null=True, blank=True)

    def __str__(self):
        return self.title
