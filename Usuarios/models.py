from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models

class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('El correo electrónico es obligatorio')
        if not username:
            raise ValueError('El nombre de usuario es obligatorio')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)  # Encriptar la contraseña
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(email, username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Usuario(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)

    objects = UsuarioManager()

    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    
