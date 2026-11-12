from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=100)
    initial = models.CharField(max_length=2, blank=True, null=True)

    def __str__(self):
        return self.name

class AboutStats(models.Model):
    figures = models.PositiveIntegerField()
    description = models.CharField(max_length=255)
    subset = models.CharField(max_length=1, blank=True, null=True)

    def __str__(self):
        return self.description

class HomeStats(models.Model):
    figures = models.PositiveIntegerField()
    description = models.CharField(max_length=255)
    subset = models.CharField(max_length=1, blank=True, null=True)

    def __str__(self):
        return self.description

class HomeServices(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    image_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title

class WhyUs(models.Model):
    details = models.CharField(max_length=255)

    def __str__(self):
        return self.details

class Services(models.Model):
    image_id = models.CharField(max_length=100)
    icon_id = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    extras = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title

class Reviews(models.Model):
    description = models.CharField(max_length=255)
    initial = models.CharField(max_length=1)
    name = models.CharField(max_length=100)
    client_type = models.CharField(max_length=255)

    def __str__(self):
        return self.name