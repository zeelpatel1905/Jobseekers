from django.urls import path
from .views import Company_Home_View, Login_view, Logout_view, Add_Employee_view
app_name = "Company"

urlpatterns = [
    path('', Company_Home_View, name='Home'),
    path('login', Login_view, name='Login'),
    path('logout', Logout_view, name='Logout'),
    path('addnewemployee', Add_Employee_view, name='Addnewemployee'),
]