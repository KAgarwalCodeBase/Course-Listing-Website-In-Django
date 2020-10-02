from django.urls import path
from . import views
app_name= "App1"
urlpatterns = [
    path('<int:couse_id>/',views.detail,name='detail'),
    path('',views.Courses,name='home-page'),
    path('<int:couse_id>/yourchoice', views.yourchoice, name='yourchoice'),

]