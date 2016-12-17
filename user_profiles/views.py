from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from models import UserProfile
from forms import UpdateProfileForm

# Create your views here.

# Login required to use this model

@login_required
def my_profile(request):
    current_profile = UserProfile.objects.get(user=request.user)
    if request.method == "GET":
        # Use a django generated form from the models.
        # Note the initial keyword is to pre populate the values, that will
        # allow users to see what the values are before updating.
        current_user_bio =  current_profile.bio
        return render(request, 'music/profile.html', {'bio': current_user_bio})

@login_required
def update_profile(request):
    current_profile = UserProfile.objects.get(user=request.user)
    if request.method == "POST":
        form = UpdateProfileForm(request.post)
        if form.is_valid():
            bio = form.cleaned_data['bio']
            current_profile.bio = bio
            current_profile.save()
            return redirect('music/profile.html')

@login_required
def profile(request, profile_id):
    if request.user.is_authenticated:
        userProfile = UserProfile.objects.get(user=request.user)
        return render(request, 'music/profile.html', {'userProfile': userProfile})

