from django.db import models
from django.db.models import Avg


class Book(models.Model):
    name = models.CharField(max_length=255)
    rating = models.IntegerField(null=True)

    def __str__(self):
        return '{0} - {1}'.format(self.pk, self.name)


class Literator(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name='literators', blank=True)

    def __str__(self):
        return '{0} - {1}'.format(self.pk, self.name)


class Vote(models.Model):
    RATING_CHOICES = CHOICES = [(i, i) for i in range(1, 6)]  # choices 1-5
    value = models.PositiveIntegerField(choices=RATING_CHOICES)
    book = models.ForeignKey(Book, related_name='votes', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '{0} - {1}'.format(self.value, self.book.name)
