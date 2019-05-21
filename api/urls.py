from django.urls import path

from . import views

urlpatterns = [
    path('test/', views.test, name='test'),

    path('bank/', views.banklist, name='banklist'),
    path('bank/<str:pk>', views.bankDetail, name='bankDetail'),
    #path('bank/<slug:bank>/<str:city>', views.test, name='test'),
    path('branch/', views.branchList, name='branchlist'),
    path('branch/<str:pk>', views.branchDetail, name='branhcDetail'),

    path('', views.index, name='index'),
]