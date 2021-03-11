from django.db import models

class Tvshow(models.Model):
    title = models.CharField(max_length=50)
    network = models.CharField(max_length=15)
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"id={self.id}, title={self.title}, network={self.network}, release date={self.release_date}, description={self.description}"