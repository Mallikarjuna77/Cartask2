from django.contrib import admin
from django.urls import path
from .views import Home, Search, Showroom, add
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', Home),
    path('search/<str:CarName>/', Search),
    path('showroom/<str:Name>/', Showroom),
    path('add new car/', add),

]