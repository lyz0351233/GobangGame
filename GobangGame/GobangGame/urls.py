from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from game.views import user_dashboard  # 新增用户面板视图导入

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', include('registration.urls')),
    path('game/', include('game.urls')),
    path('user_dashboard/', user_dashboard, name='user_dashboard'),  # 新增用户面板路径
]