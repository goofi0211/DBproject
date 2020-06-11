"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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


from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import  url

from shop.views import test,about_view,commodity_create_view, shop_view,commodity_sql_view,order_view
from employee.views import employee_view
from customer.views import customer_view
from distributor.views import d_detail_view,distributor_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', shop_view),
    path('shop/', shop_view),
    path('about/', about_view),
    path('shop/create', commodity_create_view),
    path('shop/search', commodity_sql_view),
    path('shop/order', order_view),
    path('employee/', employee_view),
    path('customer/', customer_view),
    path('distributor/', distributor_view),
    path('distributor/<int:id>/<str:name>/', d_detail_view , name='distributor_detail')
]

# 今日重點，是我們能夠讀取到圖片的關鍵
# 將存取路徑正確地導到圖片存放的路徑
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)