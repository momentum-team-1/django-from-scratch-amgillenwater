from django.db import models
from users.models import User
# Create your models here.
class Habit(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='habits')
    goal = models.CharField(max_length=260)
    goal_quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.goal

class DailyRecord(models.Model):
    habit = models.ForeignKey(to=Habit, on_delete=models.CASCADE, related_name='records')
    quantity = models.PositiveIntegerField()
    recorded_on = models.DateField(auto_now=True)
    
    class Meta():
        unique_together=[['habit', 'recorded_on']]

