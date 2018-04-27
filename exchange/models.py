from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class Course(models.Model):
    title = models.CharField(max_length=100, null=True)
    code = models.CharField(max_length=20, null=True)

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
    price = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=13, validators=[RegexValidator(r'\d{13}', 'ISBN must be 13 digits')], null=True)
    condition = models.CharField(max_length=2, choices=CONDITION_CHOICES, default=LIKE_NEW)
    notes = models.CharField(max_length=100, null=True)
    cover_Image_URL = models.URLField(max_length=400, null=True)

    def get_absolute_url(self):
        return reverse('exchange:course_listings', kwargs={'pk': self.course.pk})

    def __str__(self):
        return self.title
