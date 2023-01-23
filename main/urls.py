from django.urls import path, include

from . import views

app_name = "main"
urlpatterns = [
    path('', views.index, name='index'),
    path('position/<int:pk>/', views.positionDetail.as_view(), name='desiredposition_detail'),
]