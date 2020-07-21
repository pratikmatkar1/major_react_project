from django.urls import path
from .import views
from .views import UserApiView1

urlpatterns = [
    path('submit/', views.submitUser1, name="signupbtn"),
    path('', views.signup),
    path('apilogin/', UserApiView1.as_view()),
    path('apilogin/<int:pk>', UserApiView1.as_view()),
]