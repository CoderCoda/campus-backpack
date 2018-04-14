from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User


class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=20)

    def __str__(self):
        return self.code


class Textbook(models.Model):
    NEW = 'N'
    LIKE_NEW = 'LN'
    VERY_GOOD = 'VG'
    GOOD = 'G'
    ACCEPTABLE = 'A'
    CONDITION_CHOICES = (
        (NEW, 'New'),
        (LIKE_NEW, 'Like New'),
        (VERY_GOOD, 'Very Good'),
        (GOOD, 'Good'),
        (ACCEPTABLE, 'Acceptable')
    )

    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    #ISBN = models.PositiveIntegerField(null=True)
    condition = models.CharField(max_length=2, choices=CONDITION_CHOICES, default=LIKE_NEW)
    notes = models.CharField(max_length=100, null=True)
    cover_image_URL = models.CharField(max_length=200, null=True)

    def get_absolute_url(self):
        return reverse('exchange:course_listings', kwargs={'pk': self.course.pk})

    def __str__(self):
        return self.title
