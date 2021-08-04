from django.contrib import admin
from django.urls import path
admin.autodiscover()

from . import views

urlpatterns = [
	# /artpieces/
    #path('url', connect to views, name of the path)
    path('', views.home, name='home'),

    # /artpieces/[number_id]/
    #path(r'^(?p<album_id>[0-9]+)/$', views.detail, name="detail"),
    path('<int:number_id>/', views.detail, name="detail"),
    
    # /artpieces/login_reg.html/
    path('login_reg.html', views.login_reg, name='login_reg page'),
]