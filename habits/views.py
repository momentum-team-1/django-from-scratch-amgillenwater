from django.shortcuts import render, redirect

# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        return redirect(to='habit_list')
    return render(request,"habits/home.html")

def habit_list(request):
    habits = request.user.habits.all()
    return render(request, "habits/habit_list.html", {'habits': habits}) 