from django.db import models


class Mail(models.Model):
    """
    A model for the Contact form.
    """
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=50, blank=False, null=False)
    message = models.TextField(max_length=500, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
