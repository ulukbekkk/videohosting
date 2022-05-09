from django.db import models
from django.urls import reverse


class Category(models.Model):
    slug = models.SlugField(max_length=50, unique=True)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.genre

    def get_absolute_url(self):
        # http://test/object111/
        return reverse('video_list_by_category',
                       args=[self.slug, ])


class Video(models.Model):
    user = models.ForeignKey('myuser.User', related_name='video', on_delete=models.CASCADE, blank=True)
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
        return reverse('video_detail_url',
                       args=[self.slug, ])

    def save(self):
        self.slug = self.title.lower().replace(" ", '-')
        return super().save()


class Comment(models.Model):
    class Meta:
        db_table = 'comments'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    user = models.ForeignKey('myuser.User', related_name='comment', on_delete=models.CASCADE, blank=True)
    video = models.ForeignKey(Video, related_name='comment', on_delete=models.CASCADE, blank=True)
    text = models.TextField('Текст комментария', max_length=500)
    create_at = models.DateTimeField(auto_now_add=True)
    moder = models.BooleanField(default=False)
