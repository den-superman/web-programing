from django.shortcuts import render, redirect
from .forms import*
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import Http404

def profile_view(request, username=None):
    if username:
        profile = get_object_or_404(User, username=username).profile
    else:
        try:
            profile = request.user.profile
        except:
            raise Http404()
        
    posts = profile.user.posts.all()
    
    context = {
        'profile' : profile,
        'posts': posts
        
    }
    
    return render(request, 'ausers/profile.html',context)


def profile_edit_view(request):
    form = ProfileForm(instance=request.user.profile)
    
    if request.method =='POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
        
    return render(request, 'ausers/profile_edit.html', {'form': form})

def profile_delete_view(request):
     return render(request, 'ausers/profile_delete.html' )