from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from settings.views import index
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name ='index_page')
]
