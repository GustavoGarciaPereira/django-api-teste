#from django.conf.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('musics/', views.MusicList.as_view(), name='music-list'),
    path('algum/', views.AlgumList.as_view(), name='algum-list'),
    path('music/<int:pk>/', views.MusicDetail.as_view(), name='music-detail'),

]