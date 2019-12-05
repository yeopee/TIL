from django.shortcuts import render , redirect,get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import CustomAuthenticationForm, CustomUserCreationForm


def follow(request, user_id):
    fan = request.user
    star = get_object_or_404(id=user_id)
    if fan.stars.filter(id=star.id).exists():
        fan.stars.remove(star)
    else:
        fan.stars.add(star)
    return redirect('accounts:user_detail',star.id)

def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            
            if form.is_valid():
                user = form.save()
                auth_login(request, user)
                return redirect('board:article_list')
        else:
            form = CustomUserCreationForm()
        
        context = {'form':form}
        
        return render(request,'signup.html',context)
    else:
        return redirect('board:article_list')
def login(request):
    if request.user.is_authenticated:
        return redirect('board:article_list')
    else:        
        if request.method == 'POST':
            form = CustomAuthenticationForm(request, request.POST)
            
            if form.is_valid():
                user = form.get_user()
                auth_login(request, user)
                return redirect(request.GET.get('next') or 'board:article_list')
        else:
            form = CustomAuthenticationForm()
        
        context = {'form':form}
        
        return render(request,'login.html',context)

def logout(request):
    auth_logout(request)
    return redirect('board:article_list')