from django.shortcuts import render, redirect, get_object_or_404
from users.models import User
from habits.models import DailyRecord, Habit
from django.contrib.auth.decorators import login_required
from .forms import HabitForm

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
def habit_detail(request, habit_pk):
    detail = get_object_or_404(request.user.habits, pk=habit_pk)
    return render(request, "habits/detail.html", {"detail": detail})

@login_required
def add_habit(request):
    if request.method == "POST":
        form = HabitForm(data=request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect(to='habit_detail', habit_pk=habit.pk)
    else:
        form=HabitForm()
    
    return render(request, "habits/add_habit.html", {"form": form})
    
