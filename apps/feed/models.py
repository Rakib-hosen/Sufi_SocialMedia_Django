from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    body =  models.CharField(max_length=1000)

    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
