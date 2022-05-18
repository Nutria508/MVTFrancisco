from django.urls import path
from familia import views


urlpatterns = [
    #path('index/', views.probandoTemplate),
    path('all_familiar/', views.all_familiar),
    path('read_familiar/<int:id>/', views.read_familiar),
    path('new_familiar/<str:name>/<str:last_name>/<str:date>/', views.new_familiar),
]