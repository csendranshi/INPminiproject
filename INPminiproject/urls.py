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
from pages.views import   card_view, scroll_view

from homepage import views as view_homepage
from authentication import views as view_auth
from education import views as view_education
from business import views as view_business
from india import views as view_india
from World import views as view_world
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view_homepage.home_view, name='home'),
    path('india/', view_india.india_view, name='india'),
    path('education/', view_education.education_view, name='education'),
    path('business/', view_business.business_view, name='business'),
    path('world/', view_world.world_view, name='world'),

    path('card/', card_view, name='card'),
    path('scroll/', scroll_view, name='scroll'),
    path('auth/', view_auth.auth, name="auth")

]
