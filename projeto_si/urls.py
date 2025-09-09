from django.contrib import admin
from django.urls import path
from app_si import views
urlpatterns = [
    path('admin/', admin.site.urls),
    #path(''), = facebook.com
    #path('devaprender/')
    path('', views.home, name="home"),
]
