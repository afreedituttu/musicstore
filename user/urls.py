from django.urls import path
from . import views

app_name = 'acc'

urlpatterns = [
    path('singup/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout_view,name='logout')
]
