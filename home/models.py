from django.db import models


class PageContent(models.Model):
    """
    A model for the homepage.
    """
    about_title = models.CharField(max_length=15, blank=False, null=False)
    about_text = models.TextField(max_length=500, blank=False, null=False)
    projects_title = models.CharField(max_length=15, blank=True, null=True)
    projects_text = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.about_title
