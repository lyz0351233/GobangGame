from django.shortcuts import render, redirect
from django.contrib.auth import login
from.forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_dashboard')  # 注册成功后跳转到用户面板（根据实际情况调整）
    else:
        form = CustomUserCreationForm()
    return render(request,'registration/register.html', {'form': form})