
from django.urls import path

from home_app import views, admin_views, user_views, worker_views

urlpatterns=[
    path('',views.home,name='home'),
    path('login_view/',views.login_view,name='login_view'),
    path('user_register/',views.user_register,name='user_register'),
    path('worker_registration/',views.worker_registration,name='worker_registration'),
    path('log_out/',views.log_out,name='log_out'),


    path('admin_home/', admin_views.admin_home, name='admin_home'),
    path('worker_view/',admin_views.worker_view,name='worker_view'),
    path('service_register',admin_views.service_register,name='service_register'),
    path('service_view',admin_views.service_view,name='service_view'),
    path('service_update<int:id>/',admin_views.service_update,name='service_update'),
    path('service_delete<int:id>/',admin_views.service_delete,name='service_delete'),
    path('customer_view/',admin_views.user_view,name='customer_view'),
    path('customer_delete<int:id>/',admin_views.user_delete,name='customer_delete'),
    path('workers_update<int:id>/',admin_views.workers_update,name='workers_update'),
    path('worker_delete<int:id>/',admin_views.delete_worker,name='worker_delete'),
    path('appointment_admin/',admin_views.appointment_admin,name='appointment_admin'),
    path('approve_appointment<int:id>/',admin_views.approve_appointment,name='approve_appointment'),
    path('reject_appointment<int:id>/',admin_views.reject_appointment,name='reject_appointment'),
    path('feedback_admin/',admin_views.feedback_admin,name='feedback_admin'),
    path('reply_feedback<int:id>/',admin_views.reply_feedback,name='reply_feedback'),
    path('bill_generate/',admin_views.bill_generate,name='bill_generate'),
    path('view_bill/',admin_views.view_bill,name='view_bill'),
    path('admin_dashboard/',admin_views.admin_dashboard,name='admin_dashboard'),



    path('user_home/',user_views.user_home,name='user_home'),
    path('view_schedule_customer',user_views.view_schedule_customer,name='view_schedule_customer'),
    path('feedback_add_user/',user_views.feedback_add_user,name='feedback_add_user'),
    path('feedback_view_user/',user_views.feedback_view_user,name='feedback_view_user'),
    path('take_appointment<int:id>/', user_views.take_appointment, name='take_appointment'),
    path('view_appointment/', user_views.view_appointment, name='view_appointment'),
    path('view_workers_customer/', user_views.view_workers_customer, name='view_workers_customer'),
    path('view_bill_user/',user_views.view_bill_user,name='view_bill_user'),
    path('bill_history/',user_views.bill_history,name='bill_history'),
    path('pay_bill<int:id>/',user_views.pay_bill,name='pay_bill'),
    path('pay_in_direct<int:id>/',user_views.pay_in_direct,name='pay_in_direct'),
    path('user_dashboard/',user_views.user_dashboard,name='user_dashboard'),


    path('worker_home/',worker_views.worker_home,name='worker_home'),
    path('schedule_delete<int:id>/',worker_views.schedule_delete,name='schedule_delete'),
    path('appointment_view_worker/',worker_views.appointment_view_worker,name='appointment_view_worker'),
    path('schedule_view/', worker_views.schedule_view, name='schedule_view'),
    path('work_schedule/', worker_views.work_schedule, name='work_schedule'),
    path('schedule_update<int:id>/',worker_views.schedule_update,name='schedule_update'),
    path('view_bill_worker/',worker_views.view_bill_worker,name='view_bill_worker'),
    path('worker_dashboard/',worker_views.worker_dashboard,name='worker_dashboard')


]