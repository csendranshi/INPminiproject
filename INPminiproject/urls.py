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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from World import views as view_world
from article import views as article_views
from authentication import views as view_auth
from business import views as view_business
from education import views as view_education
from health import views as view_health
from homepage import views as view_homepage
from india import views as view_india
from pages.views import card_view, scroll_view
from posts import views as posts_views
from previous_posts import views as view_prevpost
from profile_details import views as view_profile
from technology import views as view_tech
from users_page import views as view_users_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view_homepage.home_view, name='home'),
    path('india/', view_india.india_view, name='india'),
    path('education/', view_education.education_view, name='education'),
    path('business/', view_business.business_view, name='business'),
    path('world/', view_world.world_view, name='world'),
    path('technology/', view_tech.Technology_view, name='technology'),
    path('health/', view_health.health_view, name='health'),
    path('card/', card_view, name='card'),
    path('scroll/', scroll_view, name='scroll'),
    path('register/', view_auth.auth, name="register"),
    path('login/', view_auth.Login, name="login"),
    path('logout/', view_auth.Logout, name="logout"),
    path('profile/', view_profile.profile_view, name='profile'),
    path('posts/', posts_views.posts_view, name='posts'),
    path('previous_post/', view_prevpost.prevpost_view, name='prevpost'),
    path('article/', article_views.article_view, name='article'),
    path('userspage/', view_users_page.users_view, name='user_page'),

    path('article/<grid_category>/<section>/<unique_id>', article_views.article_view, name='article'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


