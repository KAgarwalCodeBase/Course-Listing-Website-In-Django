from django.urls import path
from . import views
urlpatterns = [
    path('<int:couse_id>/',views.detail,name='detail'),
    path('',views.Courses,name='home-page'),
]