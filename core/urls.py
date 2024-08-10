from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Auth_R_F.urls')),
    path('polls/', include('polls.urls')),
    path('SL/', include('Solo_Leveling.urls')),
    path('SL_Class/', include('SL_Class.urls')),
]
