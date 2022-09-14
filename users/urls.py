from django.urls import path
from .views import home, user_logout, register, user_login

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home, name='home'),
    path('logout/', user_logout, name='user_logout'),
    path('login/', user_login, name='user_login'),
    path('register/', register, name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)