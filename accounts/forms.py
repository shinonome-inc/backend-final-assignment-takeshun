from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
# class SignupForm(UserCreationForm):
# https://qiita.com/keita_gawahara/items/e534178d9ae89872ebab
# https://qiita.com/keishi04hrikzira/items/0c6f6343cce567a00a07


    class Meta(UserCreationForm):
        model = get_user_model()
        fields = ["username", "email", "age"] # passwordは設定しない


