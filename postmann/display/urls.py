from django.urls import path
#from .views import UserApiView
from .import views


urlpatterns = [
    path('login/', views.loginpage),
    path('submit/', views.submitUser, name="submitbtn"),
    path('', views.home),
    path('detail/', views.detail),
    path('listing/', views.listing),


]