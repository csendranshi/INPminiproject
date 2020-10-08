"""INPminiproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from pages.views import home_view, auth_view, card_view, scroll_view
from pages.views import business_view, education_view, india_view, world_view
from authentication import views as view_auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('india/', india_view, name='india'),
    path('education/', education_view, name='education'),
    path('business/', business_view, name='business'),
    path('world/', world_view, name='world'),
    path('card/', card_view, name='card'),
    path('scroll/', scroll_view, name='scroll'),
    path('auth/', view_auth.auth, name="auth")

]
