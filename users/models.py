from django.db import models
# ユーザー認証
from django.contrib.auth.models import User

#左がDBに登録、右が表示される値
GRADUATE_CHOICES = [(24,24), (25,25), (26,26), (27,27), (28,28)]

# Create your models here.
class Account(models.Model):
    # ユーザー(ユーザー名、パスワード、メールアドレス）
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    icon_image = models.ImageField(upload_to='icons/')  # Specify the directory where images will be stored
    graduate_at = models.IntegerField(choices=GRADUATE_CHOICES, verbose_name='卒業年')
    graduate_at_summer = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username