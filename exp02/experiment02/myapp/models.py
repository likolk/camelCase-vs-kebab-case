from django.db import models

# Create your models here.

class Demographics(models.Model):    
    session_id = models.UUIDField(primary_key=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ])
    education = models.CharField(max_length=20, choices=[
        ('high-school', 'High School'),
        ('bachelors', 'Bachelors'),
        ('masters', 'Masters'),
        ('phd', 'PhD'),
        ('postdoc', 'Postdoc')
    ])
    occupation = models.CharField(max_length=20, choices=[
        ('student', 'Student'),
        ('engineer', 'Engineer'),
        ('teacher', 'Teacher')
    ])
    comments = models.TextField(blank=True)
    questions = models.TextField(blank=True)
    answers = models.TextField(blank=True)
    is_correct = models.TextField(blank=True)
    time_taken = models.TextField(blank=True)

    def __str__(self):
        return str(self.session_id)
