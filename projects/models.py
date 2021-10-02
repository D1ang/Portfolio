from django.db import models

class ProjectItem(models.Model):
    """
    A model for the project items.
    """
    title = models.CharField(max_length=30, blank=False, null=False)
    codebase = models.CharField(max_length=15, blank=True, null=True)
    explanation = models.TextField(max_length=250, blank=False, null=False)
    source = models.URLField(max_length=200, blank=True, null=True)
    demo = models.URLField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='artwork', null=True, blank=True)

    def __str__(self):
        return self.title
