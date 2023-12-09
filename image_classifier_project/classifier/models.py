from django.db import models

class Result(models.Model):
    prediction = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
