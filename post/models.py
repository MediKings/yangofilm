from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model


User = get_user_model()

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
    synopsis = models.TextField()
    realisateur = models.CharField(max_length=30)
    type = models.ForeignKey('Type', on_delete=models.CASCADE)
    genre = models.ManyToManyField('Genre')
    picture = models.ImageField(upload_to='image/')
    large_picture = models.ImageField(upload_to='image/')
    video = models.FileField(upload_to='video/')
    likes = models.ManyToManyField(User, related_name='likes')
    date = models.DateTimeField(auto_now_add=True)
    slide = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Genre(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Type(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post


class Pub(models.Model):
    title = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='pubs/')

    def __str__(self):
        return self.title
