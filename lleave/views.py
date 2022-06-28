from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import LeaveApplication, type_of_leave
from django.utils.html import format_html
from .forms import LeaveAppForm , CreateUserForm
import calendar
from calendar import HTMLCalendar

# Create your views here.
@login_required
def user_view(request):
    if request.method == 'POST':
        form = LeaveAppForm(request.POST)
        if form.is_valid():
            fdate = form.cleaned_data['fdate']
            tdate = form.cleaned_data['tdate']
            type_of_leave= form.cleaned_data['type_of_leave']
            reason = form.cleaned_data['reason']
           
            
        leavereq = LeaveApplication(authuser = request.user, reason = reason, fdate = fdate, type_of_leave= type_of_leave,tdate = tdate)
        print(leavereq)
        leavereq.save()
            


    leave_data = LeaveApplication.objects.filter(authuser = request.user).order_by('-id')[::]
    leave_stat = LeaveApplication.objects.filter(authuser = request.user).order_by('-id')[:1]

    my_cal = HTMLCalendar()

    form = LeaveAppForm()
    parms = {'form': form, 'leave_data' : leave_data, 'leave_stat':leave_stat, 'calendar': my_cal}
    return render(request, 'lusers/user.html', parms)


@login_required
def manager_view(request):
    user= User.objects.all()
    leave_user_data = LeaveApplication.objects.all()
    if request.method =='POST':
        id_list = request.POST.getlist('boxes')
        id_reject = request.POST.getlist('box')

        leave_user_data.update(status=False)
        leave_user_data.update(reject = False)

        for i in id_list or id_reject:
            if i in id_list:
                LeaveApplication.objects.filter(pk=int(i)).update(status =True,pending = False)
            elif i in id_reject:
                LeaveApplication.objects.filter(pk=int(i)).update(reject =True, pending = False)

    prms = {'user' : user, 'leave_user_data':leave_user_data}
    return render(request, 'lusers/admin.html', prms)



@login_required
def profile_view(request, username):
    return HttpResponse(request, 'this is my page')




def create_user_view(request):
    form = CreateUserForm()
    
    prms = {'form' : form}
    return render(request, 'lusers/create-user-page.html', prms)