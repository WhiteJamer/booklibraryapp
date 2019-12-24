from django.db import models


class Vote(models.Model):
    RATING_CHOICES = [1, 2, 3, 4, 5]
    value = models.PositiveIntegerField(choices=RATING_CHOICES)
    book = models.ForeignKey(Book, related_name='votes', on_delete=models.CASCADE)

    def __str__(self):
        return '{0} - {1}'.format(self.value, self.book.name)


class Book(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Literator(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name='literators')

    def __str__(self):
        return self.name
