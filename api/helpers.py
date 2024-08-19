from django.db import models

class StatusChoicesStaff(models.TextChoices):
    Admin = 'Admin', 'Admin'
    Teacher = 'Teacher', 'Teacher'
    Client = 'Client', 'Client'


class StatusChoicesPb(models.TextChoices):
    DRAFT = 'DRAFT', 'DRAFT'
    PUBLIC = 'PUBLIC', 'PUBLIC'