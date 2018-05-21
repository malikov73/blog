from django.db import models
from core.models import TimeStampedModel
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Category(TimeStampedModel):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Tags(TimeStampedModel):
    tag = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.tag


class Article(TimeStampedModel):
    title = models.CharField(max_length=200)
    short_text = models.CharField('Description', max_length=200)
    text = RichTextUploadingField('Article', blank=True, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Tags = models.ManyToManyField(Tags, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='article', null=True, blank=True)

    def __str__(self):
        return self.title

    def url(self):
        return self.id
