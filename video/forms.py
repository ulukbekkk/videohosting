from django.forms import ModelForm, ValidationError
from .models import Video


class VideoForm(ModelForm):
    class Meta:
        model = Video
        exclude = ('created_at', 'updated_at', 'slug')

    def clean(self):
        slug = self.cleaned_data.get('title').lower().replace(" ", '-')
        if Video.objects.filter(slug=slug).exists():
            raise ValidationError('Slug with such name already exists!')
        return self.cleaned_data

class VVideoForm(ModelForm):
    class Meta:
        model = Video
        exclude = ('created_at', 'updated_at', 'slug')