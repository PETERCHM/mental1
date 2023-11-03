# from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Professional
from .forms import ProfessionalForm
from django.shortcuts import render, redirect
from .models import MentalHealthIssue
from .forms import MentalHealthIssueForm
from django.views.decorators.csrf import csrf_protect


def home(request):
    return render(request, 'landing.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def forums(request):
    return render(request, 'forums.html')

@csrf_protect
def login_view(request):
    if request.method == 'POST':
        # Handle login form submission
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard') 
        else:
            # Handle login error
            return render(request, 'login.html', {'error_message': 'Invalid login credentials'})

    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        # Handle registration form submission
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Or, you can redirect to the login page
            return redirect('login')  

    return render(request, 'register.html')

# @login_required
def create_professional(request):
    if request.method == 'POST':
        form = ProfessionalForm(request.POST, request.FILES)
        if form.is_valid():
            professional = form.save(commit=False)
            professional.user = request.user  # Set the user to the currently logged-in user
            professional.save()
            return redirect('professional_profile', pk=professional.pk)
    else:
        form = ProfessionalForm()
    return render(request, 'create_professional.html', {'form': form})

def professional_profile(request, pk):
    professional = Professional.objects.get(pk=pk)
    return render(request, 'professional_profile.html', {'professional': professional})

# views.py
# from django.shortcuts import render, redirect
# from .models import MentalHealthIssue
# from .forms import MentalHealthIssueForm

def create_mental_health_profile(request):
    if request.method == 'POST':
        form = MentalHealthIssueForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('mental_health_profile', pk=profile.pk)
    else:
        form = MentalHealthIssueForm()
    return render(request, 'mental_health_form.html', {'form': form})

def mental_health_profile(request, pk):
    profile = MentalHealthIssue.objects.get(pk=pk)
    return render(request, 'mental_health_profile.html', {'profile': profile})
