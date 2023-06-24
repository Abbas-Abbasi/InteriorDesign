from django.db import models


# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='images')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class TeamMember(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title
