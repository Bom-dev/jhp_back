from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    goal = models.CharField(max_length=50)
    start_date = models.DateField(auto_now=False)
    end_date = models.DateField(auto_now=False)
    
    def __str__(self):
        return self.email
    
class Application(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='applications'
    )
    title = models.CharField(max_length=100, default='No Title')
    date = models.DateField(auto_now=False)
    counter = models.PositiveIntegerField(default=1)
    comment = models.CharField(max_length=200, default='No Comment')
    
    def __str__(self):
        return self.title
    
class Interview(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='interviews'
    )
    title = models.CharField(max_length=100, default='No Title')
    date = models.DateTimeField(auto_now=False)
    comment = models.CharField(max_length=200, default='No Comment')
    
    def __str__(self):
        return self.title
    
class Event(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='events'
    )
    title = models.CharField(max_length=100, default='No Title')
    date = models.DateTimeField(auto_now=False)
    comment = models.CharField(max_length=200, default='No Comment')
    
    def __str__(self):
        return self.title
    
class Study(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='studies'
    )
    title = models.CharField(max_length=100, default='No Title')
    date = models.DateField(auto_now=False)
    comment = models.CharField(max_length=200, default='No Comment')
    
    def __str__(self):
        return self.title
    
class History(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='histories'
    )
    strat_date = models.DateField()
    end_date = models.DateField()
    applications = models.JSONField()
    applications_number = models.IntegerField()
    interviews = models.JSONField()
    events = models.JSONField()
    studies = models.JSONField()
    
    def __str__(self):
        return self.strat_date