from django.db import models
from django.urls import reverse


class Category(models.Model):
    slug = models.SlugField(max_length=50, unique=True)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.genre

    def get_absolute_url(self):
        # http://test/object111/
        return reverse('video:video_list_url')
                       # args=[self.slug, ])


class Video(models.Model):
    category = models.ForeignKey(Category, related_name='video', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    prava = models.BooleanField(default=True)
    year = models.DateTimeField()
    image = models.ImageField(upload_to='image')
    video = models.FileField(upload_to='video/%y')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title', )
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        # http://test/object111/
        return reverse('video:video_detail_url',
                       args=[self.slug, ])

    def save(self):
        self.slug = self.title.lower().replace(" ", '-')
        return super().save()



