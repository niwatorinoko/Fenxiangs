from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from .models import Account

class LoginForm(AuthenticationForm):
    """ログインフォーム"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


# フォームクラス作成
class AccountForm(forms.ModelForm):
    # パスワード入力：非表示対応
    password = forms.CharField(widget=forms.PasswordInput(),label="パスワード")
    password_confirmation = forms.CharField(widget=forms.PasswordInput(), label="パスワード確認")

    class Meta():
        # ユーザー認証
        model = User
        # フィールド指定
        fields = ('username','email','password','password_confirmation')
        # フィールド名指定
        labels = {'username':"ユーザーID",'email':"メール"}
    
    prefix = 'account'

class AddAccountForm(forms.ModelForm):
    class Meta():
        # モデルクラスを指定
        model = Account
        fields = ('last_name','first_name','icon_image','graduate_at','graduate_at_summer')
        labels = {'last_name':"苗字",'first_name':"名前",'icon_image':"写真アップロード",'graduate_at':'卒業年','graduate_at_summer':'夏卒or冬卒'}

    prefix = 'add'