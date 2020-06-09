from django import forms
from .models import Habit

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields =[
            'goal',
            'goal_quantity_num',
            'goal_quantity_unit',
        ]

class RecordForm(forms.ModelForm):
    class Meta:
        model= DailyRecord
        fields= [
            'recorded_on', 
            'quantity_complete', 
            'check_mark'
        ]