from django.urls import path, include
from .views import AllFoodViews,get_food
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    path('list-of-food/',AllFoodViews.as_view()),
    path('get-recoomended-food/',get_food,name="food data"),

]
urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)