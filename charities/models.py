from django.db import models
from django.db.models import Q

from accounts.models import User


class Benefactor(models.Model):
    EXPERIENCE_CHOICES = (
        (0, "Beginner"),
        (1, "Intermediate"),
        (2, "Advanced"),
    )

    free_time_per_week = models.PositiveSmallIntegerField(default=0)
    experience = models.SmallIntegerField(choices=EXPERIENCE_CHOICES, default=0)

    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)


class Charity(models.Model):
    reg_number = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50)

    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)


class TaskManager(models.Manager):
    def related_tasks_to_charity(self, user):
        return Task.objects.filter(charity__user=user)

    def related_tasks_to_benefactor(self, user):
        return Task.objects.filter(assigned_benefactor__user=user)

    def all_related_tasks_to_user(self, user):
        return Task.objects.filter(
            Q(charity__user=user) | Q(assigned_benefactor__user=user) | Q(state="P")
        )


class Task(models.Model):
    objects = TaskManager()

    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
    )

    STATE_CHOICES = (
        ("P", "Pending"),
        ("W", "Waiting"),
        ("A", "Assigned"),
        ("D", "Done"),
    )

    state = models.CharField(choices=STATE_CHOICES, max_length=1, default="P")
    title = models.CharField(max_length=60)

    age_limit_from = models.IntegerField(default=0, null=True, blank=True)
    age_limit_to = models.IntegerField(default=0, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    gender_limit = models.CharField(
        choices=GENDER_CHOICES, max_length=1, blank=True, null=True
    )

    assigned_benefactor = models.ForeignKey(
        Benefactor, on_delete=models.SET_NULL, null=True
    )
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE)
