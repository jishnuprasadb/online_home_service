from django.contrib import admin

# Register your models here.
from home_app import models

admin.site.register(models.Worker)
admin.site.register(models.User)
admin.site.register(models.Login)
admin.site.register(models.Service)
admin.site.register(models.Schedule)
admin.site.register(models.Appointment)
admin.site.register(models.Feedback)
admin.site.register(models.Bill)
admin.site.register(models.CreditCard)
