from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


from accounts.models import CustomUser, GameRecord  # 检查导入路径是否正确

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

# @login_required
# def game_play(request):
#     mode = request.GET.get('mode')
#     color_choice = None
#     user_color = None
#     bot_color = None
#     friend_mode = False
#     if mode == 'ai':
#         if 'color' in request.GET:
#             user_color = request.GET['color']
#             bot_color = 'white' if user_color == 'black' else 'black'
#         else:
#             color_choice = True
#     elif mode == 'friend':
#         friend_mode = True
#     return render(request, 'game_play.html' if mode == 'ai' else 'game_play_friend.html', {
#        'mode': mode,
#         'color_choice': color_choice,
#         'user_color': user_color,
#         'bot_color': bot_color,
#         'friend_mode': friend_mode
#     })

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

    if request.method == 'POST' and 'game_result' in request.POST:
        is_win = request.POST.get('game_result') == 'win'
        opponent_type = 'AI' if mode == 'ai' else 'Friend'
        GameRecord.objects.create(user=request.user, opponent_type=opponent_type, is_win=is_win)

    return render(request, 'game_play.html' if mode == 'ai' else 'game_play_friend.html', {
       'mode': mode,
        'color_choice': color_choice,
        'user_color': user_color,
        'bot_color': bot_color,
        'friend_mode': friend_mode
    })


@login_required
def game_record(request):
    user = request.user
    # 正确使用模型字段和关联查询
    records = user.game_records.select_related('user').all()
    total_games = records.count()
    win_games = records.filter(result='WIN').count()
    win_rate = round((win_games / total_games) * 100, 2) if total_games > 0 else 0

    return render(request, 'game_record.html', {
        'records': records,
        'total_games': total_games,
        'win_games': win_games,
        'win_rate': win_rate
    })

@login_required
def contact_change(request):
    if request.method == 'POST':
        new_contact = request.POST.get('contact')
        request.user.contact = new_contact
        request.user.save()
        return redirect('user_dashboard')
    return render(request, 'contact_change.html')

@login_required
def image_change(request):
    if request.method == 'POST':
        new_image = request.FILES.get('image')
        if new_image:
            request.user.image = new_image
            request.user.save()
        return redirect('user_dashboard')
    return render(request, 'image_change.html')