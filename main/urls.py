from django.urls import path
from . import views
urlpatterns = [
    path('reviews/', views.ReviewListCreateAPIView.as_view()),
    path('reviews/<int:id>/', views.ReviewUpdateDeleteAPIView.as_view()),
    path('register/', views.RegisterAPIView.as_view())
]