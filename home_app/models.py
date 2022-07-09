from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Login(AbstractUser):
    is_user = models.BooleanField(default=False)
    is_worker = models.BooleanField(default=False)


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Worker(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='worker', null=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    work_type = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class User(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='user')
    name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name


class Schedule(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointment')
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)


class Feedback(models.Model):
    user = models.ForeignKey(Login, on_delete=models.DO_NOTHING)
    subject = models.CharField(max_length=200)
    feedback = models.TextField()
    date = models.DateField()
    reply = models.TextField(null=True, blank=True)


class Bill(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    bill_date = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    paid_on = models.DateField(auto_now=True)
    status = models.IntegerField(default=0)


class CreditCard(models.Model):
    card_no = models.CharField(max_length=30)
    card_cvv = models.CharField(max_length=30)
    expiry_date = models.CharField(max_length=200)
