from django.db import models
from django.utils import timezone


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    # slug = models.SlugField(unique=True, default='', max_length=100, blank=True, null=True)
    content = models.TextField(blank=False)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length = 50)
    image = models.ImageField(default='default_profile_picture.jpg', upload_to='blog_images', blank=True, null=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# def pre_save_receiver(sender, instance, *args, **kwargs): 
#     if not instance.slug: 
#         instance.slug = unique_slug_generator(instance) 

  
# pre_save.connect(pre_save_receiver, sender = BlogPost) 