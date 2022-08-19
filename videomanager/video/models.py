from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.



class TitleManager(MPTTModel):
    title = models.CharField(max_length=50, unique=True,help_text="Name of title of video")
    slug = models.SlugField(unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        full_path = [ self.title ]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' -> '.join(full_path[ ::-1 ])

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class VideoManager(models.Model):
    title= models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    videofile= models.FileField(upload_to='videos/%Y/%m/%d/', null=True, verbose_name="")
    video_description= models.CharField(max_length=500,blank=True,null=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    parent_title = models.ForeignKey(TitleManager,on_delete=models.CASCADE)

    class Meta:
        ordering = ['-timestamp']

    def get_absolute_url(self):
        return reverse("video_list", kwargs={"slug":self.slug})

    def __str__(self):
        return self.title + ": " + str(self.id)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

