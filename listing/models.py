from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Listing(models.Model):
    STATUS_CHOICES = (
        ('drafts', 'Drafts'),
        ('published', 'Published'),
    )
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique_for_date='publish')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='business_logo', blank=True)
    cover = models.ImageField(upload_to='business_cover', blank=True)
    about = models.CharField(max_length=500, unique=True)
    service = models.TextField()
    address = models.CharField(max_length=200, blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='drafts')

    class Meta:
        ordering = ('-publish',)
        verbose_name = 'listing'
        verbose_name_plural = 'listings'

    def get_absolute_url(self):
        return reverse('list_detail', args=[self.publish.year,
                                            self.publish.month,
                                            self.publish.day,
                                            self.slug])

    def __str__(self):
        return self.name

class Review(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)
        verbose_name = 'review'
        verbose_name_plural = 'reviews'

    def __str__(self):
        return self.name


