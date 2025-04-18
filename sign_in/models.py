from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}, Email: {self.email}, Password: {self.password}"
