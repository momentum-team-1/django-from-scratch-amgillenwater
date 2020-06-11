from django.shortcuts import render, redirect, get_object_or_404
from users.models import User
from habits.models import DailyRecord, Habit
from django.contrib.auth.decorators import login_required
from .forms import HabitForm, RecordForm
from datetime import date,datetime
from django.views.generic.edit import UpdateView

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
    habit = get_object_or_404(request.user.habits, pk=habit_pk)
    return render(request, "habits/habit_detail.html", {"habit": habit})

@login_required
def add_habit(request):
    if request.method == 'POST':
        form = HabitForm(data=request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect(to='habit_list')
    else:
        form=HabitForm()
    
    return render(request, "habits/add_habit.html", {"form": form})

@login_required
def delete_habit(request, habit_pk):
    habit = get_object_or_404(request.user.habits, pk=habit_pk)
    if request.method == 'POST':
        habit.delete()
        return redirect(to='habit_list')

    return render(request, "habits/delete_habit.html", {"habit": habit})

@login_required
def new_record(request, habit_pk):
    habit = get_object_or_404(request.user.habits, pk=habit_pk)
    record = habit.records.filter(recorded_on=date.today()).first()
    if request.method == 'POST':
        form = RecordForm(data=request.POST, instance=record)
        if form.is_valid():
            record = form.save(commit=False)
            record.habit = habit
            record.save()
            return redirect(to='habit_detail', habit_pk=habit.pk)

    else:
        form=RecordForm(instance=record)
    
    return render(request,"habits/new_record.html", {'form':form,'habit':habit,'record':record})


