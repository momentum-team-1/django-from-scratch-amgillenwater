from django.db import models
from users.models import User
# Create your models here.
class Habit(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='habits')
    verb = models.CharField(max_length=260)
    goal_quant = models.PositiveIntegerField(null=True,blank=True)
    
    # def __str__(self):

class DailyRecord(models.Model):
    habit = models.ForeignKey(to=Habit, on_delete=models.CASCADE, related_name='records')
    recorded_on = models.DateField(auto_now=True)


