from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from home_app.forms import WorkerRegister, LoginRegister, ServiceRegister, AddBill
from home_app.models import Worker, Login, User, Service, Appointment, Feedback, Bill


@login_required(login_url='login_view')
def admin_home(request):
    return render(request, 'admin_temp/admin_home.html')


@login_required(login_url='login_view')
def admin_dashboard(request):
    return render(request, 'admin_temp/dashboard.html')


@login_required(login_url='login_view')
def worker_view(request):
    w = Worker.objects.all()
    context = {
        'data': w
    }
    return render(request, 'admin_temp/worker_view.html', context)


@login_required(login_url='login_view')
def workers_update(request, id):
    w = Worker.objects.get(id=id)
    l = Login.objects.get(worker=w)
    if request.method == 'POST':
        form = WorkerRegister(request.POST or None, instance=w)
        user_form = LoginRegister(request.POST or None, instance=l)
        if form.is_valid() and user_form.is_valid():
            form.save()
            user_form.save()
            messages.info(request, 'workers updated successful')
            return redirect('worker_view')
    else:
        form = WorkerRegister(instance=w)
        user_form = LoginRegister(instance=l)
    return render(request, 'admin_temp/worker_update.html', {'form': form, 'user_form': user_form})


@login_required(login_url='login_view')
def delete_worker(request, id):
    data1 = Worker.objects.get(id=id)
    data = Login.objects.get(worker=data1)
    if request.method == 'POST':
        data.delete()
        return redirect('worker_view')
    else:
        return redirect('worker_view')


@login_required(login_url='login_view')
def user_view(request):
    c = User.objects.all()
    context = {
        'data': c
    }
    return render(request, 'admin_temp/customer_view.html', context)


@login_required(login_url='login_view')
def user_delete(request, id):
    data1 = User.objects.get(id=id)
    data = Login.objects.get(user=data1)
    if request.method == 'POST':
        data.delete()
        return redirect('customer_view')
    else:
        return redirect('customer_view')


@login_required(login_url='login_view')
def service_register(request):
    service_form = ServiceRegister()
    if request.method == 'POST':
        service_form = ServiceRegister(request.POST)
        if service_form.is_valid():
            service_form.save()
            return redirect('service_register')
    return render(request, 'admin_temp/service_register.html', {'service_form': service_form})


@login_required(login_url='login_view')
def service_view(request):
    s = Service.objects.all()
    context = {
        'data': s
    }
    return render(request, 'admin_temp/service_view.html', context)


@login_required(login_url='login_view')
def service_update(request, id):
    obj = Service.objects.get(id=id)
    form = ServiceRegister(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('service_view')
    else:
        form = ServiceRegister(instance=obj)
    return render(request, 'admin_temp/service_update.html', {'form': form})


@login_required(login_url='login_view')
def service_delete(request, id):
    data = Service.objects.get(id=id)
    data.delete()
    return redirect('service_view')


@login_required(login_url='login_view')
def appointment_admin(request):
    a = Appointment.objects.all()
    context = {
        'appointment': a,
    }
    return render(request, 'admin_temp/appointment.html', context)


@login_required(login_url='login_view')
def approve_appointment(request, id):
    a = Appointment.objects.get(id=id)
    a.status = 1
    a.save()
    messages.info(request, 'Appointment  Confirmed')
    return redirect('appointment_admin')


@login_required(login_url='login_view')
def reject_appointment(request, id):
    n = Appointment.objects.get(id=id)
    n.status = 2
    n.save()
    messages.info(request, 'Appointment Rejected')
    return redirect('appointment_admin')


@login_required(login_url='login_view')
def feedback_admin(request):
    f = Feedback.objects.all()
    return render(request, 'admin_temp/complaint_view.html', {'feedback': f})


@login_required(login_url='login_view')
def reply_feedback(request, id):
    f = Feedback.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        f.reply = r
        f.save()
        messages.info(request, 'Reply send for complaint')
        return redirect('feedback_admin')
    return render(request, 'admin_temp/reply_complaint.html', {'feedback': f})


@login_required(login_url='login_view')
def bill_generate(request):
    form = AddBill()
    if request.method == 'POST':
        form = AddBill(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_bill')
    return render(request, 'admin_temp/generate_bill.html', {'form': form})


@login_required(login_url='login_view')
def view_bill(request):
    bill = Bill.objects.all()
    return render(request, 'admin_temp/view_payment_details.html', {'bills': bill})
