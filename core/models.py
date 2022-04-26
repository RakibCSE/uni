from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    message = models.TextField(max_length=256)

    def __str__(self):
        return f'{self.name}-{self.email}'


class Book(models.Model):
    name_b = models.CharField(max_length=256)
    email_b = models.EmailField(max_length=256)
    phone_b = models.CharField(max_length=256)
    comments_b = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.name_b} {self.email_b}'
