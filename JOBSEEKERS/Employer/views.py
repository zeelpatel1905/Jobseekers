from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from .models import Employee,Job_upload
from  .forms import EmployeeForm, LoginForm, add_new_password_form, forgot_password_form, otp_match_form, JobuploadForm
from django.views.generic.list import ListView
from itertools import chain
import random



# Create your views here.
def Company_Home_View(request):
    Temp = "Employer\index.html"
    if request.session.get('email') == None:
        return redirect("Company:Login")
    return render(request, Temp)


def Add_Employee_view(request):
    template = "Employer/AddEmployee.html"
    if request.method == 'POST':
        print("In post")
        form = EmployeeForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            print("Is Valid")
            f = form.save(commit=False)
            email = request.POST.get('emp_email')
            name = request.POST.get('emp_name')
            subject = 'Hello ' + str(name) + ' From JobSeekers'
            message = "stay connected. we would love to hear from you    http://127.0.0.1:8000/company_admin/login"
            email_from = settings.EMAIL_HOST_USER
            email_to = [email, ]
            send_mail(subject, message, email_from, email_to)

            data = Employee.objects.filter(emp_email= request.session.get('email'))
            f.emp_company = data.emp_company
            print(f.emp_company)
            f.save()
            messages.success(request, 'data Enter Done !!')
            return redirect('Company:Home')
    else:
        messages.error(request, 'Please Correct the error below.')
        form = EmployeeForm()
    return render(request, template , {'employee_form': form})


def Add_new_job(request):
    template = "Employer/AddJob.html"
    if request.method == 'POST':
        form = JobuploadForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            f = form.save(commit=False)
            data = Employee.objects.filter(emp_email= request.session.get('email'))
            print(data)
            data1 = Employee.objects.values('emp_company_id')
            print(data1)
            f.comapny_id_id = data1

            #print(data.emp_company_id)
            print(f.comapny_id_id)
            f.save()
            messages.success(request, 'data Enter Done !!')
            return redirect('Company:Home')
    else:
        messages.error(request, 'Please Correct the error below.')
        form = JobuploadForm()
    return render(request, template , {'job_upload_form': form})




def Login_view(request):
    template = "Employer/Employer authentication/login.html"
    if request.method == 'POST':
        login = LoginForm(request.POST or None)
        email = request.POST.get('emp_email')
        password = request.POST.get('emp_password')
        is_email = Employee.objects.filter(emp_email__iexact=email).exists()
        is_pass = Employee.objects.filter(emp_password__iexact=password).exists()
        if is_email and is_pass:
            request.session['email'] = email
            data = Employee.objects.get(emp_email = email)
            is_super = data.is_super_emp
            print(is_super)
            request.session['super'] = is_super
            print(data)
            return redirect('Company:Home')
    else:
        login = LoginForm()
    return render(request, template, {'login_form':login})



def Logout_view(request):
    if request.session.get('email') != None:
        request.session.delete()
    else:
        return redirect('Company:Login')

    template = "Employer/Employer authentication/logout.html"
    return render(request, template, {})


def Forgot_password(request):
    temp = "Employer/Employer authentication/forget_password.html"
    if request.method == 'POST':
        f_p_form = forgot_password_form(request.POST)
        if f_p_form.is_valid():
            email = request.POST.get('email')
            is_email = Employee.objects.filter(emp_email__iexact=email).exists()
            if is_email:
                OTP = random.randint(111111,999999)

                #email OTP send Logic
                subject = "Password Reset OTP @JOBSEEKER"
                message = "Your OTP is, " + str(OTP) + " .Please Follow This Link, --> http://127.0.0.1:8000/Company/Home"
                email_from = settings.EMAIL_HOST_USER
                email_to = [email,]
                send_mail(subject,message,email_from,email_to)
                #email OTP done

                #OTP and email set In Session
                request.session["reset_password_OTP"] = OTP
                request.session["reset_password_EMAIL"] = email
                return redirect('Company:Enter_otp')
    else:
        f_p_form = forgot_password_form()

    return render(request,temp, {'form':f_p_form})


def Otp_match(request):
    temp = "Employer/Employer authentication/enter_otp.html"
    if request.method == 'POST':
        e_otp_form = otp_match_form(request.POST)
        if e_otp_form.is_valid():
            otp = request.POST.get('otp')
            session_otp = request.session.get('reset_password_OTP')
            if str(otp) == str(session_otp):
                return redirect('Company:Add_New_Password')
    else:
        e_otp_form = otp_match_form()

    return render(request, temp, {'form':e_otp_form})


def Add_new_password(request):
    temp = "Employer/Employer authentication/Add_new_password.html"
    if request.method == 'POST':
        add_password_form = add_new_password_form(request.POST)
        if add_password_form.is_valid():
            passwd = request.POST.get('c_password')
            print(passwd)
            email = request.session.get('reset_password_EMAIL')
            print(email)
            Employee.objects.filter(emp_email = email).update(emp_password = passwd)
            request.session.delete()
            return redirect('Company:Login')
    else:
        add_password_form = add_new_password_form()

    return render(request,temp, {'form':add_password_form})

class ViewJob(ListView):
    paginate_by = 15
    template_name = 'Employer/ViewJobList.html'

    def get_queryset(self):
        job = Job_upload.objects.all().order_by("job_upload_date")

        job_list = sorted(
            chain(job),
            key=lambda Job_upload: Job_upload.job_upload_date, reverse=True)
        return job_list

def EditJob(request, pk):
    template = 'Employer/EditJob.html'
    job = get_object_or_404(Job_upload, pk=pk)
    form = JobuploadForm(request.POST or None, request.FILES or None, instance=job)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Edited!')
        return redirect('Company:ViewJob')
    return render(request, template, {'job_upload_form': form})

def DeleteJob(request, pk):
    template = 'Employer/DeleteJob.html'
    job = get_object_or_404(Job_upload, pk=pk)
    if request.method == 'POST':
        job.delete()
        return redirect('Company:ViewJob')
    return render(request, template, {'object': job})

