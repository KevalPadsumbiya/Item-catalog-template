from django.urls import path
from . import views

urlpatterns = [
	path('',views.index,name="index"),
	path('confirm-and-pay',views.pay,name="pay"),
	path('success',views.last,name="last"),
]