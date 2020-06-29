from django.db import models
from users.models import User
from datetime import date
# Create your models here.
class Habit(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='habits')
    goal = models.CharField(max_length=260, help_text="What habit do you want to build?(ex--read)")
    goal_quantity_num = models.PositiveIntegerField(default=0, help_text="What is your numeric goal for your daily habit? (ex--50)")
    goal_quantity_unit = models.CharField(max_length=260, help_text="What unit of measure are you using for your goal? (ex. pages)")
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.goal}{self.goal_quantity_num}{self.goal_quantity_unit}"

class DailyRecord(models.Model):
    habit = models.ForeignKey(to=Habit, on_delete=models.CASCADE, related_name='records')
    quantity_complete = models.PositiveIntegerField(default=0)
    recorded_on = models.DateField(default=date.today)
    check_mark = models.BooleanField(default=False)
    
    class Meta:
        unique_together=['habit', 'recorded_on']
    
    def __str__(self):
        return f"{self.recorded_on} {self.quantity_complete}"

