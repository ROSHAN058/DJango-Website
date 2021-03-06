"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls import url
from django.contrib import admin
from .views import (search)

from automation.admin import event_admin_site
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', admin.site.urls),
    path('index',views.index,name='index'),
    path('about', views.about, name='about'),
    path('Upload', views.Upload, name='Upload'),
    path('company', views.company, name='company'),
    path(
    'admin/password_reset/',
    auth_views.PasswordResetView.as_view(),
    name='admin_password_reset',
),
    path(
    'admin/password_reset/done/',
    auth_views.PasswordResetDoneView.as_view(),
    name='password_reset_done',
),
    path(
    'reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(),
    name='password_reset_confirm',
),
    path(
    'reset/done/',
    auth_views.PasswordResetCompleteView.as_view(),
    name='password_reset_complete',
),


    path('event-admin/', event_admin_site.urls),
    path('microsoft/', include('microsoft_auth.urls', namespace='microsoft')),
    path(r'^advanced_filters/', include('advanced_filters.urls')),
    url(r'^search/$', views.search, name='search'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


