from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    is_admin = forms.BooleanField(required=False, label='注册为管理员')
    contact = forms.CharField(max_length=100, required=False, label='联系方式')  # 新增联系方式字段

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'is_admin', 'contact']  # 添加 contact 到字段列表