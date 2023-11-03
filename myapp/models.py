from django.db import models
from django.contrib.auth.models import User

class Professional(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255,default='')
    last_name = models.CharField(max_length=255,default='')
    email = models.EmailField(unique=True, default= 'example@gmail.com')
    password = models.CharField(max_length=255,default='')
    confirm_password = models.CharField(max_length=255, default='')
    location = models.CharField(max_length=255,default='')
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')],default='')
    specialization = models.CharField(max_length=255)
    experience = models.PositiveIntegerField()
    education = models.TextField()
    skills = models.TextField()
    certification = models.TextField()
    portfolio_url = models.URLField()
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    licenses = models.TextField(default='')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    user = models.OneToOneField(User, on_delete=models.CASCADE)

class MentalHealthIssue(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    location = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    description = models.TextField()
    diagnosis_date = models.DateField()
    treatment_plan = models.TextField()
    support_network = models.TextField()
    additional_information = models.TextField()
