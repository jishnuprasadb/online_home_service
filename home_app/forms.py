import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from home_app.models import Login, User, Worker, Service, Schedule, Feedback, Bill, CreditCard


class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')


def phone_number_validator(value):
    if not re.compile(r'^[7-9]\d{9}$').match(value):
        raise ValidationError('This is Not a Valid Phone Number')


class UserRegister(forms.ModelForm):
    phone_number = forms.CharField(validators=[phone_number_validator])

    class Meta:
        model = User
        fields = ('name', 'phone_number', 'email', 'address')


class WorkerRegister(forms.ModelForm):
    phone_number = forms.CharField(validators=[phone_number_validator])

    class Meta:
        model = Worker
        fields = ('name', 'phone_number', 'email', 'address', 'work_type')


class ServiceRegister(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('name', 'amount')


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class ScheduleForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    start_time = forms.TimeField(widget=TimeInput)
    end_time = forms.TimeField(widget=TimeInput)

    class Meta:
        model = Schedule
        fields = ('date', 'start_time', 'end_time')


class FeedbackForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)

    class Meta:
        model = Feedback
        fields = ('subject', 'feedback', 'date')


class AddBill(forms.ModelForm):
    class Meta:
        model = Bill
        exclude = ('status', 'paid_on')


class PayBillForm(forms.ModelForm):
    card_no = forms.CharField(validators=[RegexValidator(regex='^.{16}$', message='Please Enter a Valid Card No')])
    card_cvv = forms.CharField(widget=forms.PasswordInput,
                               validators=[RegexValidator(regex='^.{3}$', message='Please Enter a Valid CVV')])
    expiry_date = forms.DateField(widget=DateInput(attrs={'id': 'example-month-input'}))

    class Meta:
        model = CreditCard
        fields = ('card_no', 'card_cvv', 'expiry_date')
