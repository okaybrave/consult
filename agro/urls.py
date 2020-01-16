from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .import views
from .views import successView

urlpatterns = [
	path('',views.home, name='home_index.html'),
	path('service/',views.serv, name='service.html'),
	path('about/',views.about, name='about_us.html'),
	path('contact/',views.emailview, name='contact_us.html'),
	path('success/',successView, name='success'),
]
urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)