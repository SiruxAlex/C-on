"""hackathon URL Configuration

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
from lotteon.views import *

urlpatterns = [
    path('wtfisthewinner/', admin.site.urls),
    path('creator-center-main/', CCmain.as_view()),
    path('creator-market-ad-complete/', CMAcomplete.as_view()),
    path('creator-market-ad-proposal/', CMAproposal.as_view()),
    path('creator-market-detail/', CMdetail.as_view()),
    path('creator-market-detail-1/', CMdetail1.as_view()),
    path('creator-market-main/', CMmain.as_view()),
    path('creator-market-main-1/', CMmain1.as_view()),
    path('creator-market-mypage/', CMmypage.as_view()),
    path('creator-market-register-1/', CR1.as_view()),
    path('creator-market-register-2/', CR2.as_view()),
    path('creator-market-register-3/', CR3.as_view()),

]
