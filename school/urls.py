from django.contrib import admin
from django.urls import path
from asosiy.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view()),
    path('post/<int:id>/', OnePost.as_view()),
    path('about/', About.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
