from django.urls import path,include
from . import views 
urlpatterns = [
    path('wattsup',views.testfun,name='wattsup')
]
