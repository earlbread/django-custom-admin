from django.db import models


class User(models.Model):
    email = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)


class UserForChangingEmail(User):
    class Meta:
        proxy = True

    def __str__(self):
        return "이메일 변경 유저"


class EmailChangeRequest(models.Model):
    user = models.ForeignKey(UserForChangingEmail)
    new_email = models.CharField(max_length=255)
    id_card = models.FileField()

