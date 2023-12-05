from django.db import models

# Create your models here.

class Demographics(models.Model):    
    session_id = models.UUIDField(primary_key=True)
    age = models.IntegerField()
    experience = models.CharField(max_length=20, choices=[
        ('yes', 'Yes'),
        ('no', 'No'),
    ] )
    comments = models.TextField(blank=True)
    questions = models.TextField(blank=True)
    answers = models.TextField(blank=True)
    is_correct = models.TextField(blank=True)
    time_taken = models.TextField(blank=True)

    def __str__(self):
        return str(self.session_id)
