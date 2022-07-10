"""link_shortening URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from links.views import UserRegisterView, UserLoginView, MyLinksView, ShortLinkRedirectView, custom_handler404, \
    custom_handler500, \
    MainView, UserLogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='home'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('mylinks/', MyLinksView.as_view(), name='mylinks'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('<slug:url_hash>/', ShortLinkRedirectView.as_view(), name='redirect'),

]

handler404 = custom_handler404
handler500 = custom_handler500
