from django.urls import path, include
from .views import User_Home_View, Edit_profile, View_profile, Job_list, Job_detail
app_name = "Employee"

urlpatterns = [
    path('', User_Home_View, name='Home'),
    path('editprofile', Edit_profile, name='EditProfile'),
    path('profile', View_profile, name='Profile'),
    path('joblist', Job_list.as_view(), name='JobList'),
    path('jobdetail/<int:pk>', Job_detail , name="JobDetail"),
]