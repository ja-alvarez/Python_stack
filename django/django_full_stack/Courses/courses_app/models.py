from __future__ import unicode_literals
from django.db import models

class NewCourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors["name"] = "Course name should be at least 5 characters"
        if len(postData['description']) < 15:
            errors["desc"] = "Course description should be at least 15 characters"
        return errors

class NewCourse(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField() #null=True, blank=True
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = NewCourseManager()