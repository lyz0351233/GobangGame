from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def user_dashboard(request):
    """用户功能界面视图"""
    return render(request, 'user_dashboard.html')

@login_required
def game_home(request):
    return render(request, 'game_home.html')


@login_required
def game_match(request):
    return render(request, 'game_match.html')


from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def game_play(request):
    mode = request.GET.get('mode')
    color_choice = None
    user_color = None
    bot_color = None
    friend_mode = False
    if mode == 'ai':
        if 'color' in request.GET:
            user_color = request.GET['color']
            bot_color = 'white' if user_color == 'black' else 'black'
        else:
            color_choice = True
    elif mode == 'friend':
        friend_mode = True
    return render(request, 'game_play.html' if mode == 'ai' else 'game_play_friend.html', {
       'mode': mode,
        'color_choice': color_choice,
        'user_color': user_color,
        'bot_color': bot_color,
        'friend_mode': friend_mode
    })

@login_required
def game_record(request):
    return render(request, 'game_record.html')
