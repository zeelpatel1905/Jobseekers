from django.urls import path
from .views import Company_Home_View, Login_view, Logout_view
app_name = "Company"

urlpatterns = [
    path('', Company_Home_View, name='Home'),
    path('login', Login_view, name='Login'),
    path('logout', Logout_view, name='Logout'),
]