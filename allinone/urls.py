from django.contrib import admin
from django.urls import path , include
from . import views
urlpatterns = [
    path('game/', views.game, name='game'),
    path('', views.index, name='index'),
    path('app/', views.app_view, name='app'),
    path('specific_app/<str:category>/<str:subcat>', views.specific_app, name='specific_app'),
    path('app-detail/<int:id>/', views.app_detail, name='app-detail'),
    path('rate/<int:id>/<int:rate>', views.rate, name='rate'),
      path('increasedownload/', views.increase_download, name='increase_download'),
      path('search/', views.search, name='search'),
]
