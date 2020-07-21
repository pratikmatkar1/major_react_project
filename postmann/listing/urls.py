from django.urls import path
from .views import RestaurantView

urlpatterns = [
    path('list1/', RestaurantView.as_view()),
    path('list1/<int:pk>',RestaurantView.as_view()),
]
