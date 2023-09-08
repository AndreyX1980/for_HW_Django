from django.contrib import admin
from django.urls import path, include

from HW_3.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prefix/', include('HW_1.urls')),
    path ('les3/', include ('HW_3.urls')),
    path ('les4/', include ('HW_4.urls')),
    path ('', index),
    # path('__debug__/', include("debug_toolbar.urls")),
    path ('les6/', include ('HW_6.urls')),
]