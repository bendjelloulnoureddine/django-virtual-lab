from django.db import models

class DockerSession(models.Model):
    path        = models.CharField(max_length=255)

    def __str__(self):
        return self.path
