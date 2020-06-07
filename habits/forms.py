from django import forms
from .models import Habit, DailyRecord

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields =[
            'user',
            'goal',
            'goal_quantity',
        ]