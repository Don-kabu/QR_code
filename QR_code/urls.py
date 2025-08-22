"""
URL configuration for QR_code project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from qr_code.views import create_document,home,document_list,visit_link
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("document/new/",create_document,name="document_new"),
    path("document/",document_list,name="document_list"),
    path("scan/<str:id>",visit_link),
    # path("document/scan/",create_document,name="scan"),
    path("",home,name="home",)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
