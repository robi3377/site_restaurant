from django.shortcuts import redirect, render
from .models import Mancare, Feedback

def index(request):
    feedback = Feedback.objects.all()
    return render(request, 'index.html', {'feedback': feedback})

def about(request):
    return render(request, 'about.html')

def menu(request):
    mancare = Mancare.objects.all()
    return render(request, 'menu.html', {'mancare': mancare})

def feedback(request):
    feedback_primit = request.POST['feedback']
    feedback_nou = Feedback.objects.create(text = feedback_primit)
    feedback_nou.save()
    return redirect('index')

