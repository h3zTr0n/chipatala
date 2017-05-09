"""chipatala URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from login.views import index

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    url(r'^admin/', admin.site.urls),
    url(r'^prescriptions/', include('prescriptions.urls')),
    url(r'^appointment/', include('appointment.urls')),
    url(r'^registration/', include('registration.urls')),
    url(r'^logs/', include('logs.urls')),
    url(r'^testResult/', include('testResult.urls')),
    url(r'^messaging/', include('messaging.urls')),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'} ),
    url(r'^login/', include('login.urls')),
    url(r'^search/', include('search.urls')),
    url(r'^$', index),
]
