from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'music'
urlpatterns = [
    path('',views.index.as_view(),name='index'),
    path('music/<slug:pk>/',views.detail.as_view(),name='detail'),
    path('add/',views.add.as_view(),name='add'),
    path('update/',views.update.as_view(),name='update'),
    path('/<slug:pk>/delete',views.delete,name='delete'),
    path('register',views.register.as_view(),name='register'),
    path('/<slug:pk>/addsong',views.addsong,name='addsong'),
    path('music/<slug:pk>/delete',views.detail.as_view(),name='detail'),
    path('<slug:id>/<slug:name>/songdelete',views.songdelete,name='songdelete'),
]