from __future__ import unicode_literals
from django.db import models
from datetime import datetime

class TvshowManager(models.Manager):
    def basic_validator (self, postData):
        errors = {}
        if len(Tvshow.objects.filter(title=postData['title']))>0:
            errors['exists'] = 'TV Show already registered!'
        else: 
            if len(postData['title']) < 2:
                errors['title'] = 'Title should be at least 2 characters.'
            if len(postData['network']) < 3:
                errors['network'] = 'Network should be at least 3 characters.'
#Al comentar todo desde acá hasta return puedo agregar info en la BBDD
#            if (postData['release_date'] == None):
#                errors['release_date'] = 'Please indicate the release date'
#            else:
#                date = postData['release_date']
#                release_date = datetime.strptime(date, "%Y-%m-%d")
#                today = datetime.now()
#                if release_date > today:
#                    errors['release_date'] = 'Wrongly entered date.'
            if len(postData['description']) != 0:
                if len(postData['description']) < 10:
                    errors['description'] = 'Description should be at least 10 characters.'
        return errors #this return! xd

class Tvshow(models.Model):
    title = models.CharField(max_length=50)
    network = models.CharField(max_length=15)
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TvshowManager()