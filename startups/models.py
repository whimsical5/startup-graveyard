from django.db import models
from django.utils.text import slugify

class Startup(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    industry = models.CharField(max_length=100, blank=True, null=True)
    failure_reason = models.TextField(blank=True, null=True)
    lessons_learned = models.TextField(blank=True, null=True)
    founded_year = models.PositiveIntegerField(blank=True, null=True)
    closed_year = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


