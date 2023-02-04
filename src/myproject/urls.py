"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from myproject import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('me/<str:company>/<str:name>', views.get_user_info),
    path('card/<str:company>/<str:name>/<int:card>', views.get_card_info),
    path('modify/<str:company>/<str:name>/<int:card_number>/<int:new_limit>', views.modify_limit),
    path('create/<int:number>/<str:name>/<str:company>/<str:expiration_date>/<int:masked_number>/<int:limit>/<int:balance>/<str:permission>', views.create_card),
]