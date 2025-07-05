from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, email, full_name=None, role=None, phone=None, ward_no=None, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            full_name=full_name,
            role=role,
            phone=phone,
            ward_no=ward_no,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name=None, role=None, phone=None, ward_no=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, full_name, role, phone, ward_no, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    ward_no = models.PositiveIntegerField()
    
    # New fields
    position = models.CharField(max_length=100, verbose_name="पद", null=True, blank=True)
    department = models.CharField(max_length=100, verbose_name="महाशाखा", null=True, blank=True)
    section = models.CharField(max_length=100, verbose_name="शाखा", null=True, blank=True)
    administrative_level = models.CharField(max_length=100, verbose_name="रा. प्र. स्तह", null=True, blank=True)
    
    # Status and timestamps
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'role', 'phone', 'ward_no']

    objects = UserManager()

    def __str__(self):
        return self.full_name

