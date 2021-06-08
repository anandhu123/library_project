from django.db import models
from authentication.models import *

# Create your models here.
class Books(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    count = models.IntegerField()
    timestamp = models.DateTimeField(auto_now=False,
                                     auto_now_add=True)

    def __str__(self):
        return str(self.id)

class BorrowBooks(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('authentication.User',
                               on_delete=models.CASCADE)

    book = models.ForeignKey('Books',
                              on_delete=models.CASCADE)

    timestamp = models.DateTimeField(auto_now=False,
                                     auto_now_add=True)
    returned = models.BooleanField(default=False)
    returned_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.id)