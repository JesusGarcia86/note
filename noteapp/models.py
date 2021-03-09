from django.db import models

class NoteManager(models.Manager):
    def validator(self, postdata):
        errors={}
        if len(postdata['title'])<2:
            errors['title']="First Name must be longer than 2 characters!"
        if len(postdata['description'])<2:
            errors['description']="Last Name must be longer than 2 characters!"
        return errors

class Note(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = NoteManager
