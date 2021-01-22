from django.urls import path,include
from django.contrib import admin
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('news.urls')),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    url('logout/', views.logout, {"next_page": '/'}), 
    
]