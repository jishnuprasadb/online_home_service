from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from home_app.forms import ScheduleForm
from home_app.models import Worker, Schedule, Appointment, Bill


@login_required(login_url='login_view')
def worker_home(request):
    return render(request, 'worker_temp/worker_home.html')


@login_required(login_url='login_view')
def worker_dashboard(request):
    return render(request, 'worker_temp/dashboard.html')


@login_required(login_url='login_view')
def work_schedule(request):
    form = ScheduleForm()
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.worker = Worker.objects.get(user=request.user)
            form.save()
            messages.info(request, 'schedule added successful')
            return redirect('worker_home')
    return render(request, 'worker_temp/work_schedule.html', {'form': form})


@login_required(login_url='login_view')
def schedule_view(request):
    u = Worker.objects.get(user=request.user)
    s = Schedule.objects.filter(worker=u)
    context = {
        'schedule': s
    }
    return render(request, 'worker_temp/schedule_view.html', context)


@login_required(login_url='login_view')
def schedule_update(request, id):
    s = Schedule.objects.get(id=id)
    if request.method == 'POST':
        form = ScheduleForm(request.POST or None, instance=s)
        if form.is_valid():
            form.save()
            messages.info(request, 'schedule updated')
            return redirect('schedule_view')
    else:
        form = ScheduleForm(instance=s)
    return render(request, 'worker_temp/schedule_update.html', {'form': form})


@login_required(login_url='login_view')
def schedule_delete(request, id):
    s = Schedule.objects.filter(id=id)
    if request.method == 'POST':
        s.delete()
        return redirect('schedule_view')


@login_required(login_url='login_view')
def appointment_view_worker(request):
    a = Appointment.objects.all()
    return render(request, 'worker_temp/appointment_view.html', {'appointment': a})


@login_required(login_url='login_view')
def view_bill_worker(request):
    bill = Bill.objects.all()
    return render(request, 'worker_temp/view_payment_details.html', {'bills': bill})
