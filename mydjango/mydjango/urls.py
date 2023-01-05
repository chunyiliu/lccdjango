"""mydjango URL Configuration

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

from news.views import news,index
from product.views import shop
from message.views import contact
from performance.views import performance
from abouts.views import aboutme
from cart.views import cart,addtocart,cartorder,cartok,cartordercheck,myorder,ECPayCredit
from member.views import login,logout,register,manage
from photos.views import uploadFile

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("news/",news),
    path("product/",shop),
    path("message/",contact),
    path("performance/",performance),
    path("abouts/",aboutme),
    path("cart/",cart),
    path("addtocart/<str:ctype>/",addtocart),
    path("addtocart/<str:ctype>/<int:productid>/",addtocart),
    path("cartorder/",cartorder),
    path("cartok/",cartok),
    path("cartordercheck/",cartordercheck),
    path("login/",login),
    path("logout/",logout),
    path("register/",register),
    path("member/",manage),
    path("myorder/",myorder),
    path('creditcard/',ECPayCredit),
    path("photos/",uploadFile),
    path('',index),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

