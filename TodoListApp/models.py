from django.db import models

# Create your models here.

class Todo (models.Model):
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('pending','Pending')
    ]

    description = models.CharField(max_length=100)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description