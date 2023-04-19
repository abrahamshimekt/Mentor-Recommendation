from django.db import models
from django.contrib.auth.models import User

class Mentor(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500)
    location = models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to='mentor_profile_pictures', null=True, blank=True)
    hourly_rate = models.DecimalField(max_digits=5, decimal_places=2)
    schedule = models.ManyToManyField('Schedule',related_name='mentors')
    group_sessions = models.ManyToManyField('GroupSession', related_name='mentors', blank=True)
    skills = models.ManyToManyField('Skill')

    def __str__(self):
        return self.user.username

class Skill(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Schedule(models.Model):

    mentor = models.ForeignKey(Mentor, related_name='schedules', on_delete=models.CASCADE)
    day_of_week = models.IntegerField(choices=[(i, i) for i in range(1, 8)])
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f'{self.mentor.user.username} - {self.day_of_week} - {self.start_time} to {self.end_time}'

class GroupSession(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.name

class Feedback(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    session = models.ForeignKey(GroupSession, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f'{self.student.user.username} - {self.mentor.user.username} - {self.session.name}'

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500)
    location = models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to='student_profile_pictures', null=True, blank=True)
    interests = models.ManyToManyField('Interest')

    def __str__(self):
        return self.user.username

class Interest(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
