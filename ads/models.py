from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):
    LOCATION_CHOICES = [
        ('Karachi', 'Karachi'),
        ('Lahore', 'Lahore'),
        ('Multan', 'Multan'),
    ]
    name = models.CharField(
        max_length=100,
        choices=LOCATION_CHOICES,
        default='Karachi',
        unique=True,
    )
    max_daily_visitors = models.PositiveIntegerField()
    users_per_day = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Ad(models.Model):
    ad_name = models.CharField(max_length=100, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    locations = models.ManyToManyField(Location, choices=Location.LOCATION_CHOICES)

    def __str__(self):
        return self.ad_name

class CreateUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username

class UserVisit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} visited {self.ad.ad_name}'

class FileStored(models.Model):
    date = models.DateField()
    content = models.TextField()
    file = models.FileField(upload_to='files/', default='default_value_here')

    def save(self, *args, **kwargs):
        super(FileStored, self).save(*args, **kwargs)

    def __str__(self):
        return f"File for {self.date}"

