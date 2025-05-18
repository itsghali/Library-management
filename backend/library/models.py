from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    available = models.BooleanField(default=True)

    class Meta:
        app_label = 'library'

    def __str__(self):
        return self.title

class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    class Meta:
        app_label = 'library'

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reserved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'library'