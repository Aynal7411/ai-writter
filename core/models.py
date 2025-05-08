# portfolio/models.py
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField()  # e.g., 90 for 90%

    def __str__(self):
        return self.name
