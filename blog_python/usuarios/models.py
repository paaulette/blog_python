from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Por favor ingresar un e-mail')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=email,
            username=username,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(max_length=254, blank=True, null=True, unique=True)
    is_admin = models.BooleanField(default=False)
    fecha_registro = models.DateTimeField(default=timezone.now)
    descripcion = models.CharField(max_length=500, blank=True, null=True)
    web = models.CharField(max_length=500, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.username

# class Avatar (models.Model):
   
#     user = models.ForeignKey(User, on_delete=models.CASCADE)    
#     imagen = models.ImageField(upload_to='avatares/', null=True, blank = True)
 
#     def __str__(self):
#         return f"{self.user} - {self.imagen}"