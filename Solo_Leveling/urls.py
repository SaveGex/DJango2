from django.urls  import path


from . import views

app_name = "SL"

urlpatterns = [
    path('', views.common, name='common'),
    path('ep/', views.index, name='index'),
]