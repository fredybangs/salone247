from django.db import models


class Categories(models.Model):
    category_name = models.CharField(max_length=100)
    category_logo = models.CharField(max_length=250)

    def __str__(self):
        return self.category_name


class Song(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=50)
    song_title = models.CharField(max_length=250)
    album_title = models.CharField(max_length=250)
