from django.urls import path

from system import views

urlpatterns = [
    path('slider/list/', views.slider_list, name="slider_list"),
]