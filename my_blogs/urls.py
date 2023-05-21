"""
URL configuration for my_blogs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap

from .sitemaps import CategorySitemap, PostSitemap

from core.views import frontpage, about, robots_txt
from authenticator.views import signin, signup, signout, activate

sitemaps = {'category': CategorySitemap, 'post': PostSitemap}

urlpatterns = [
    path('sitemap.xml', sitemap, {"sitemaps": sitemaps},name="django.contrib.sitemaps.views.sitemap"),
    path('robots.txt', robots_txt, name='robots_txt'),
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('signout/', signout, name='signout'),
    path('activate/<uidb64>/<token>', activate, name='activate'),
    path('', include('blog.urls')),
    path('', frontpage, name='frontpage'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)