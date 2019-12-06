from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Event(models.Model):
    name = models.CharField(max_length=100, blank='True', default='')
    slug = models.SlugField(blank=True, default='')
    description = models.TextField(blank=True)
    start_date = models.DateTimeField(blank=True)
    end_date = models.DateTimeField(blank=True)
    attendees = models.IntegerField(blank=True, default=0)
    created = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)
    creator = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='events')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['start_date']


# class Register(models.Model):
#     name = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='events')
#
#     def __str__(self):
#         return self.name
#
#     def save(self, *args, **kwargs):  # new
#         if not self.slug:
#             self.slug = slugify(self.name)
#         return super().save(*args, **kwargs)
