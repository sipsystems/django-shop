from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:course_id>', views.single_course, name='single_course'),
    path('register', views.register_request, name='register'),
    path('login', views.login_shop, name='login')
]
