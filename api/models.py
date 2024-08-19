from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import EmailField, CharField, TextField, URLField

from .helpers import StatusChoicesStaff, StatusChoicesPb


class User(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    email = EmailField(unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    image = models.URLField(max_length=500, blank=True)
    stage = models.IntegerField(default=0)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user',
        verbose_name='user permissions',
    )

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['phone_number']),
        ]

    def __str__(self):
        return self.first_name


class Staffs(User):
    status_choices = models.CharField(max_length=20, choices=StatusChoicesStaff.choices,
                                      default=StatusChoicesStaff.Client)

    class Meta:
        verbose_name = 'Staff'
        verbose_name_plural = 'Staffs'
        ordering = ['id']
        indexes = [
            models.Index(fields=['status_choices']),
        ]


class ServicesCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField(max_length=500)
    status = models.CharField(max_length=15, choices=StatusChoicesPb.choices, default=StatusChoicesPb.PUBLIC)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['status']),
        ]

    def __str__(self):
        return self.name


class Services(models.Model):
    name = models.CharField(max_length=100)
    entry_moto = CharField(max_length=100)
    description = models.TextField()
    image = models.URLField(max_length=500)
    category = models.ForeignKey(ServicesCategory, on_delete=models.CASCADE)
    staffs = models.ManyToManyField(User)
    status = models.CharField(max_length=15, choices=StatusChoicesPb.choices, default=StatusChoicesPb.PUBLIC)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['status']),
        ]

    def df_to_pb(self):
        if self.status == 'DRAFT':
            self.status = 'PUBLIC'
            self.save()

    def pb_to_df(self):
        if self.status == 'PUBLIC':
            self.status = 'DRAFT'
            self.save()

    def __str__(self):
        return self.name


class Blog(models.Model):
    name = models.CharField(max_length=100)
    entry_moto = CharField(max_length=100)
    description = models.TextField()
    image = models.URLField(max_length=500)
    status = models.CharField(max_length=15, choices=StatusChoicesPb.choices, default=StatusChoicesPb.PUBLIC)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['status']),
        ]

    def df_to_pb(self):
        if self.status == 'DRAFT':
            self.status = 'PUBLIC'
            self.save()

    def pb_to_df(self):
        if self.status == 'PUBLIC':
            self.status = 'DRAFT'
            self.save()

    def __str__(self):
        return self.name


class About(models.Model):
    our_status = TextField()
    experience = TextField()
    description = models.TextField()
    image = models.URLField(max_length=500)
    staffs = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    services = models.ForeignKey(Services, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    telephone_number = CharField(max_length=15, unique=True)
    status = models.CharField(max_length=15, choices=StatusChoicesPb.choices, default=StatusChoicesPb.PUBLIC)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)

    class Meta:
        ordering = ['our_status']
        indexes = [
            models.Index(fields=['telephone_number']),
            models.Index(fields=['status']),
        ]

    def __str__(self):
        return self.our_status


class Applications(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone_number = models.CharField(max_length=15, unique=True)
    project = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    status = models.CharField(max_length=15, choices=StatusChoicesPb.choices, default=StatusChoicesPb.PUBLIC)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)

    class Meta:
        ordering = ['full_name']
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['telephone_number']),
            models.Index(fields=['status']),
        ]

    def __str__(self):
        return self.full_name
