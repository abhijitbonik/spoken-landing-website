"""spoken_main_website URL Configuration

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
from django.urls import include, path
from django.conf.urls import url
from spoken import views as spoken_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('spoken/', include('spoken.urls')),
    path('api/jobfairs/', spoken_views.JobFairList.as_view()),
    path('sso/', include('sso.urls', namespace='sso')),
    path('logs/', include('logs.urls', namespace='logs')),
    url(r'^$', spoken_views.home, name='home'),
    path('logout/', spoken_views.logout_view, name='logout_view'), 
    path('dashboard/', spoken_views.dashboard, name='dashboard'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
