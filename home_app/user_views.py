from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from home_app.forms import FeedbackForm, PayBillForm
from home_app.models import Worker, Schedule, User, Appointment, Feedback, Bill, CreditCard


@login_required(login_url='login_view')
def user_home(request):
    return render(request, 'user_temp/user_home.html')


@login_required(login_url='login_view')
def user_dashboard(request):
    return render(request, 'user_temp/dashboard.html')


@login_required(login_url='login_view')
def view_workers_customer(request):
    data = Worker.objects.all()
    return render(request, 'user_temp/workers.html', {'data': data})


@login_required(login_url='login_view')
def view_schedule_customer(request):
    s = Schedule.objects.all()
    context = {
        'schedule': s
    }
    return render(request, 'user_temp/schedule_view.html', context)


@login_required(login_url='login_view')
def take_appointment(request, id):
    s = Schedule.objects.get(id=id)
    u = User.objects.get(user=request.user)
    appointment = Appointment.objects.filter(user=u, schedule=s)
    if appointment.exists():
        messages.info(request, 'you have already requested appointment')
        return redirect('view_schedule_customer')
    else:
        if request.method == 'POST':
            obj = Appointment()
            obj.user = u
            obj.schedule = s
            obj.save()
            messages.info(request, 'Appointment booked successfully')
            return redirect('view_schedule_customer')
    return render(request, 'user_temp/take_appointment.html', {'appointment': s})


@login_required(login_url='login_view')
def view_appointment(request):
    u = User.objects.get(user=request.user)
    a = Appointment.objects.filter(user=u)
    return render(request, 'user_temp/appointment.html', {'appointment': a})


@login_required(login_url='login_view')
def feedback_add_user(request):
    form = FeedbackForm()
    u = request.user
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
            messages.info(request, 'Complaint Registered Successfully')
            return redirect('feedback_view_user')
    return render(request, 'user_temp/complaint_add.html', {'form': form})


@login_required(login_url='login_view')
def feedback_view_user(request):
    f = Feedback.objects.filter(user=request.user)
    return render(request, 'user_temp/complaint_view.html', {'feedback': f})


@login_required(login_url='login_view')
def view_bill_user(request):
    u = User.objects.get(user=request.user)
    bill = Bill.objects.filter(name=u)
    return render(request, 'user_temp/view_bill_user.html', {'bills': bill})


@login_required(login_url='login_view')
def pay_bill(request, id):
    bill = Bill.objects.get(id=id)
    if request.method == 'POST':
        card = request.POST.get('card')
        c = request.POST.get('cvv')
        da = request.POST.get('exp')
        CreditCard(card_no=card, card_cvv=c, expiry_date=da).save()
        bill.status = 1
        bill.save()
        messages.info(request, 'Bill Paid  Successfully')
        return redirect('bill_history')
    return render(request, 'user_temp/pay bill.html')


@login_required(login_url='login_view')
def pay_in_direct(request, id):
    bill = Bill.objects.get(id=id)
    bill.status = 2
    bill.save()
    messages.info(request, 'Chosen to Pay Fee Direct in office')
    return redirect('bill_history')


@login_required(login_url='login_view')
def bill_history(request):
    u = User.objects.get(user=request.user)
    bill = Bill.objects.filter(name=u, status__in=[1, 2])

    return render(request, 'user_temp/view_bill_history.html', {'bills': bill})
