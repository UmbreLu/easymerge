from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    pwhash = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    sheet = models.URLField(max_length=200)

    def __str__(self):
        return self.name
