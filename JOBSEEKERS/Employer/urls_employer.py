from django.urls import path
from .views import Company_Home_View, Login_view, Logout_view, Add_Employee_view, Forgot_password, Add_new_password, Otp_match, Add_new_job
app_name = "Company"

urlpatterns = [
    path('', Company_Home_View, name='Home'),
    path('login', Login_view, name='Login'),
    path('logout', Logout_view, name='Logout'),
    path('addnewemployee', Add_Employee_view, name='Addnewemployee'),
    path('Forgot_password', Forgot_password, name="Forgot_password"),
    path('Add_new_password', Add_new_password, name="Add_New_Password"),
    path('Enter_otp', Otp_match, name="Enter_otp"),
    path('Add_new_job', Add_new_job , name="Add_Job"),

]