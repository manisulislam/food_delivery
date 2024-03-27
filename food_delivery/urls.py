
from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('food/delivery/', include('delivery_app.urls')),
]
urlpatterns+=staticfiles_urlpatterns()
