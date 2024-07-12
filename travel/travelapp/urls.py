from . import views

from django.urls import path

urlpatterns = [
   path ('', views.demo, name='demo'),
  # path('add/',views.addition,name='addition'),
  # path('sub/',views.subtract,name='subtract'),
   #path('mul/',views.multiply,name='multiply'),
  # path('div/',views.quotient,name='division'),
  #  path('op/',views.operations,name='operations')

]