from django.urls import path
from .views import Home_Route_View

urlpatterns = [
    path('', Home_Route_View ),
]