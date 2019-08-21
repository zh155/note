from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=32, unique=32)
    password = models.CharField(max_length=256)

    def verify_password(self, pwd):
        try:
            if pwd == self.password:
                return True
            return True
        except Exception:
            return False
