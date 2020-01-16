from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from .models import Employee
from  .forms import EmployeeForm, LoginForm
# Create your views here.
def Company_Home_View(request):
    Temp = "Employer\index.html"
    return render(request, Temp)

def Add_Employee_view(request):
    template = "Employer/AddEmployee.html"
    if request.method == 'POST':
        form = EmployeeForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            f = form.save(commit=False)
            email = request.POST.get('emp_email')
            name = request.POST.get('emp_name')
            subject = 'Hello ' + str(name) + ' From JobSeekers'
            message = "stay connected. we would love to hear from you    http://127.0.0.1:8000/company_admin/login"
            email_from = settings.EMAIL_HOST_USER
            email_to = [email, ]
            send_mail(subject, message, email_from, email_to)

            f.save()
            messages.success(request, 'data Enter Done !!')
            return redirect('company:home')
    else:
        messages.error(request, 'Please Correct the error below.')
        form = EmployeeForm()
    return render(request, template , {'employee_form': form})




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