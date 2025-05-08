from django.contrib import admin
from django.templatetags.static import static
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from game.views import user_dashboard  # 新增用户面板视图导入

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', include('registration.urls')),
    path('game/', include('game.urls')),
    path('user_dashboard/', user_dashboard, name='user_dashboard'),  # 新增用户面板路径
]

# 开发环境下的静态文件和媒体文件配置
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)