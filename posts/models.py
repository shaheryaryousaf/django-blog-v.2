from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.contrib.auth.models import User


# ============================
# Unique Slug Function
# ============================


def generate_unique_slug(klass, field):
    origin_slug = slugify(field)
    unique_slug = origin_slug
    numb = 1
    while klass.objects.filter(slug=unique_slug).exists():
        unique_slug = '%s-%d' % (origin_slug, numb)
        numb += 1
    return unique_slug


# ============================
# Category
# ============================

class Category(models.Model):
    title = models.CharField(max_length=200)
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.TextField(blank=True)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        if self.slug:  # edit
            if slugify(self.title) != self.slug:
                self.slug = generate_unique_slug(Category, self.title)
        else:  # create
            self.slug = generate_unique_slug(Category, self.title)
        super(Category, self).save(*args, **kwargs)



# ============================
# Posts
# ============================

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='category_set')
    title = models.CharField(max_length=200)
    description = RichTextField()
    is_published = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)    
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.TextField(blank=True)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug:  # edit
            if slugify(self.title) != self.slug:
                self.slug = generate_unique_slug(Post, self.title)
        else:  # create
            self.slug = generate_unique_slug(Post, self.title)
        super(Post, self).save(*args, **kwargs)