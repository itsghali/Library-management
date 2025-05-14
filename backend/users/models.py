from django.contrib.auth.models import AbstractUser 
from django.db import models 
from django.utils.translation import gettext_lazy as _ 

class User(AbstractUser):
    class Roles(models.IntegerChoices):
        LIBRARIAN = 1, _('Librarian')
        MEMBER = 2, _('Member')
    
    role = models.IntegerField(choices=Roles.choices, default=Roles.MEMBER)
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username

    @property
    def is_librarian(self):
        return self.role == self.Roles.LIBRARIAN
