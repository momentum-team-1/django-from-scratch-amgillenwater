from django.shortcuts import render, redirect, get_object_or_404
from users.models import User
from habits.models import DailyRecord, Habit
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        return redirect(to='habit_list')
    
    return render(request,"habits/home.html")

@login_required
def habit_list(request):
    habits = request.user.habits.all()
    return render(request, "habits/habit_list.html", {"habits": habits}) 

@login_required
def daily_record(request, pk):
    record = get_object_or_404(request.user.habits, pk=pk)
    return render(request, "habits/daily_record.html", {"record": record})


